from ast import parse
from collections import deque
from functools import reduce
from tabnanny import check
import nltk
import re

from numpy import true_divide
from chat import chat
from random import randint

from plugins.agent_plugin import AgentPlugin
from nltk.corpus import wordnet
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#Wikipedia API
import wikipedia
#Google Maps API
import googlemaps
import json

class Agent:
    lastname = False
    prevQuery = ""
    
    #Globals for wikiSearch
    searching = False
    isMedical = False
    
    #Globals for GoogleMaps and directions function
    APIkey = "AIzaSyBkAMPW5ql7w3zcpHIg8zZVK18qaAFzqyc"
    gmaps = googlemaps.Client(APIkey)
    address = ""
    directing = False
    
    def __init__(self, plugins, nltk_dependencies):
        print("Downloading nltk dependencies")
        for dependency in nltk_dependencies:
            nltk.download(dependency)

        self.plugins = list(map(lambda x: x(), plugins))

    def query(self, query) -> str:
        #TODO: Spelling Check, call a function within agent to fix the query to realistic words --GABE or whoever gets to it
        check = self.plugins[0].parse(query)
        print(check)
        #TODO Part of speach tagging --Nathan
        pos_tag = self.plugins[1].parse(query)
        #TODO: Named Entity Recognition: Recognize names given and append
        ne_rec = self.plugins[2].parse(pos_tag) 
        #saying "hello" or "tell jessica to" or something to the front --GABE
        #TODO: COReference: Figure out if the query is about the user or their patient is talking about --Jordan C
        ##TODO Sentiment for easy interchangeable sentences
        sentiment = self.plugins[3].parse(check)

        ####TODODODO: Add all of the sections, and return Dr phils smart answer to the query all 3
        
        base = chat(check)
        base = self.sentimentAnalysis(sentiment, base)
        base = self.NER(ne_rec, query, base)
        base = self.wikiSearch(check, base)
        
        #To turn off spellcheck when we're entering an address
        if self.address == "pending":
            base = self.direction(query, base)
        else:
            base = self.direction(check, base)
        
        return base 

    
    def pos_tag(self, query):
        token = nltk.word_tokenize(query)
        tagged = nltk.pos_tag(token)
        
        return tagged
   
    
    ## self.synonyms(word, pos_tag) returns list of synonyms for inputted word with the pos_tag
    ## has error catching now
    def synonyms(self, word, pos_tag):
        word = word.lower()
        try:
            synonyms = set()
            synonyms.add(word)
            valid_sets = [s for s in wordnet.synsets(word, pos = pos_tag) if s.name().startswith(word)]
            while len(synonyms) < 3 and valid_sets:
                syn_set = valid_sets.pop(0)
                print(syn_set)
                if syn_set.name().startswith(word):
                    for l in syn_set.lemmas():
                        name = l.name().replace("_", " ")
                        synonyms.add(name.lower())

            return synonyms
        except:
            print("Encountered an error; make sure you inputted a valid word to get synonyms.")
            return word
    
    
    
    def sentimentAnalysis(self, sentiment, base):
        if(sentiment<-.5):
            oh_nos = ["I'm sorry to hear that! ",
                      "That doesn't sound very good. ",
                      "I'm sorry you feel this way. ",
                      "I hope I can help you feel better! ",
                      "Hold on, we'll get you feeling better in no time! ",
                      "I'll work my hardest to help you feel better. "]
            base = oh_nos[randint(0, len(oh_nos)-1 ) ] + base
        return base
    
    
    
    def NER(self, ne_rec, query, base):
        check = query.split()
        if len(ne_rec)>0:
            if "they" in check:
                base = "Please tell " + ne_rec[len(ne_rec)-1] + ": \"" + base + "\""
                self.lastname = True
                
            if "They" in check:
                base = "Please tell " + ne_rec[len(ne_rec)-1] + ": \"" + base + "\""
                self.lastname = True
            if "their" in check:
                base = "Please tell " + ne_rec[len(ne_rec)-1] + ": \"" + base + "\""
                self.lastname = True
                
            if "Their" in check:
                base = "Please tell " + ne_rec[len(ne_rec)-1] + ": \"" + base + "\""
                self.lastname = True
                
            if "I'm" in check:
                base = "Hello, " + ne_rec[0] + ". " + base
        else:
            if "They" in check:
                base = "Tell them: \"" + base + "\""
            if "they" in check:
                base = "Tell them: \"" + base + "\""        
        return base
    
    
    
    def wikiSearch(self, query, base):
        query = query.rstrip()
        searchQuery = re.split("look up |search for |wikipedia for", query.lower().rstrip())
        
        if self.searching and "yes" in query:
            self.searching = False
            return wikipedia.summary(wikipedia.page(self.prevQuery), sentences = 2)
        elif self.searching:
            self.searching = False
            return "If there's anything else you need just ask."
        
        if len(searchQuery) > 1:
            try:
                self.searching = True
                searchResult = wikipedia.search(searchQuery[-1])[0]
                page = wikipedia.page(searchResult, auto_suggest=False)
                categories = page.categories
            
                for category in categories:
                    if "health" in category:
                        self.isMedical = True
                        break
                
                if self.isMedical:
                    self.isMedical = False
                    self.searching = False
                    return wikipedia.summary(page, sentences = 2)
                else:
                    self.prevQuery = searchQuery[-1]
                    return "I don't think that's relevant to anybodies health. Would you like me to try and answer anyway?"
            except:
                self.searching = False
                self.isMedical = False
                return "Sorry I couldn't find what you were looking for. Try rewording what you want to search for."
        else:
            return base
        


    def direction(self, query, base):
        directionQuery = re.split("directions to| directions for |where is |location of |the nearest |the closest ", query.lower().rstrip()) 
        
        if len(directionQuery) > 1 or self.address == "pending":
            try:
                if not self.address:
                    self.prevQuery = query
                    self.address = "pending"
                    return "I'll need to know your address before I can give you directions. Make sure the address is in this format: 9999 Bigtree Street, Kelowna, BC"
                
                if self.address == "pending":
                    self.address = query
                    directionQuery = re.split("directions to |where is |location of |the nearest | the closest", self.prevQuery.lower().rstrip()) 
                    
                coordinates = self.gmaps.geocode(self.address)[0]['geometry']['location']
                lat_lng = str(coordinates['lat']) + ", " + str(coordinates['lng'])
            
                closest = self.gmaps.places(query = directionQuery[-1], location = lat_lng, radius = 10000)['results'][0]
                closest_id = closest['place_id']
            
                directions = self.gmaps.directions(origin = self.address, destination = 'place_id:' + closest_id, mode = "driving")[0]
                print(directions['legs'][0]['steps'])
            
                instructions = "Directions to " + closest['name'] + ": "
                for x in directions['legs'][0]['steps']:
                    instructions = instructions + x['html_instructions'].replace('<b>', '').replace('</b>', '').replace('<div style="font-size:0.9em">', '. ').replace('</div>', '') + ". "
            
                self.address = ""
                
                return instructions
            except:
                self.address = ""
                return "Sorry I had some trouble getting you directions. If you want me to try again just ask."
        else:
            return base   
        