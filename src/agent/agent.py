from ast import parse
from collections import deque
from functools import reduce
from tabnanny import check
import nltk
import re
from chat import chat
from random import randint

from plugins.agent_plugin import AgentPlugin
from nltk.corpus import wordnet
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#Wikipedia API
import wikipedia

class Agent:
    lastname = False
    searching = False
    isMedical = False
    prevQuery = ""
    
    def __init__(self, plugins, nltk_dependencies):
        print("Downloading nltk dependencies")
        for dependency in nltk_dependencies:
            nltk.download(dependency)

        self.plugins = list(map(lambda x: x(), plugins))

    def query(self, query) -> str:
        #return chat(query)

        print(self.plugins)
        #TODO: Spelling Check, call a function within agent to fix the query to realistic words --GABE or whoever gets to it
        check = self.plugins[0].parse(query)
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
        base = self.wikiSearch(check)
        
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
            
            print(synonyms)

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
    
    
    
    def wikiSearch(self, query):
        searchQuery = re.split("look up |search for ", query.lower())
        
        if self.searching and "yes" in query:
            self.searching = False
            return wikipedia.summary(wikipedia.search(self.prevQuery, results = 1), sentences = 3)
        elif self.searching:
            self.searching = False
            return "If there's anything else you need just ask."
        
        if len(searchQuery) > 1:
            try:
                self.searching = True
            
                searchResult = wikipedia.search(searchQuery[1], results = 1)
            
                categories = wikipedia.page(searchResult).categories
            
                for category in categories:
                    if "health" in str(category): #Find better ways to check if it's related to medicine
                        self.isMedical = True
                        break
                
                if self.isMedical:
                    self.isMedical = False
                    self.searching = False
                    return wikipedia.summary(searchResult, sentences = 3)
                else:
                    self.prevQuery = query
                    return "I don't think that's relevant to anybodies health. Would you like me to try and answer anyway?"
            except:
                self.searching = False
                self.isMedical = False
                return "Sorry I couldn't find what you were looking for. Try rewording what you want to search for."
        else:
            return query