from plugins.agent_plugin import AgentPlugin
import re
import spellchecker

class SpellCheck(AgentPlugin):
    def parse(self, query):
        spell = spellchecker.SpellChecker()
        spell.word_frequency.load_words(['covid'])
        spell.unknown(['COVID', 'covid','coronavirus',"covid-19", "wikipedia"])
        wordList = re.findall(r'\w+', query)
        pattern = re.compile(r"(.)\1{2,}")
        
        correct_query = ""
        
        for word in wordList:
            word = pattern.sub(r"\1\1", word)
            correct_query += spell.correction(word) + " "
        
        print(correct_query)
        
        return correct_query