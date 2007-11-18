import nltk.data
from nltk.tokenize import *
import syllables

class textanalyzer(object):

    tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+')
    special_chars = ['.', ',', '!', '?']
    
    def __init__(self):
        pass

    def analyzeText(self, text=''):
        
        words = self.getWords(text)
        charCount = self.getCharacterCount(words)
        wordCount = len(words)
        sentenceCount = len(self.getSentences(text))
        syllablesCount = self.countSyllables(words)
        complexwordsCount = self.countComplexWords(text)
        averageWordsPerSentence = wordCount/sentenceCount
        
        print '*' * 70
        print ' Number of characters: ' + str(charCount)
        print ' Number of words: ' + str(wordCount)
        print ' Number of sentences: ' + str(sentenceCount)
        print ' Number of syllables: ' + str(syllablesCount)
        print ' Number of complex words: ' + str(complexwordsCount)
        print ' Average words per sentence: ' + str(averageWordsPerSentence)
        print '*' * 70
    analyzeText = classmethod(analyzeText)  
        

    def getCharacterCount(self, words):
        characters = 0
        for word in words:
            characters += len(word)
        return characters
    getCharacterCount = classmethod(getCharacterCount)    
        
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
        
        
    def demo(self):
        text = """
                It is for us the living, rather,
                to be dedicated here to the unfinished
                work which they who fought here have
                thus far so nobly advanced. It is
                rather for us to be here dedicated
                to the great task remaining before us,
                that from these honored dead we take 
                increased devotion to that cause for which they
                gave the last full measure of devotion, that we
                here highly resolve that these dead shall not have
                died in vain, that this nation, under God, shall have a
                new birth of freedom, and that government of the people, by
                the people, for the people, shall not perish from this earth.  
               """
        textanalyzer.analyzeText(text)
        pass
    demo = classmethod(demo)
    
def demo():
    textanalyzer.demo()
    
if __name__ == "__main__":
    textanalyzer.demo()
    
        
        
        
        
        
    
    