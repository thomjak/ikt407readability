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
    
    def countSyllables(self, words = []):
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
        sentences = len(self.getSentences(text));
        sentencesList = self.getSentences(text);
        complexWords = 0
        found = False;
        #Just for manual checking and debugging.
        cWords = []
        curWord = []
        
        for word in words:          
            curWord.append(word)
            if self.countSyllables(curWord)>= 3:
                
                #Checking proper nouns. If a word starts with a capital letter
                #and is NOT  at the beginning of a sentence we don't add it
                #as a complex word.
                if not(word[0].isupper()):
                    complexWords += 1
                    #cWords.append(word)
                else:
                    for sentence in sentencesList:
                        if str(sentence).startswith(word):
                            found = True
                            break
                    
                    if found: 
                        complexWords+=1
                        found = False
                    
            curWord.remove(word)
        return complexWords
    countComplexWords = classmethod(countComplexWords)
        
        
        
        
        
        
        
        
        
        
    
    