import nltk
from nltk import *

class gunningfog:
    
    __text = ""
    
    def __init__(self, text=""):
        self.__text = text
        
    def setText(self,text):
        self.__text = text
        
    def calc(self):
        if len(self.__text) == 0:
            print 'No text set'
            return
        else:
            text = self.__text
        
        tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+')
        words = tokenizer.tokenize(text)
        
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        sentences = tokenizer.tokenize(text)
        
        complex_words = []
        
        print str(len(words)) + ' ' + str(len(sentences))
        print words
        
        
g = gunningfog("lala lala.\ntra lala la jiha.\nlala laaaaaaa.")
g.calc()
    