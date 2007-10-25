import nltk.data
import syllables
from nltk.tokenize import *

class textanalyzer(object):

    tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+')
    special_chars = ['.', ',', '!', '?']
    
    def __init__(self):
        pass

    def getWords(self, text=''):
        words = []
        words = self.tokenizer.tokenize(text)
        for word in words:
            if word in self.special_chars:
                words.remove(word)
        return words
    getWords = classmethod(getWords)
    
    def getSentences(self, text=''):
        sentences = []
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        sentences = tokenizer.tokenize(text)
        return sentences
    getSentences = classmethod(getSentences)
    
    def countSyllables(selfself, words = []):
        syllableCount = 0
        for word in words:
            syllableCount += syllables.count_word_fallback(word)
            
        return syllableCount
    countSyllables = classmethod(countSyllables)
    
    
    #This method must be enhanced. At the moment it only
    #considers the number of syllables in a word.
    #This often results in that too many complex words are detected.
    def countComplexWords(self, text=''):
        words = self.getWords(text)
        complexWords = 0
        #Just for manual checking and debugging.
        cWords = []
        
        for word in words:
            if self.countSyllables(word)>= 3:
                complexWords = complexWords + 1
                cWords.append(word)
                print word
        
        return complexWords
    countComplexWords = classmethod(countComplexWords)
        
        
        
        
        
        
        
        
        
        
    
    