import nltk
import nltk.tokenize

class gunninfog:
    
    __text = ""
    
    def __init__(self, text=""):
        self.__text = text
        
    def setText(self,text):
        self.__text = text
        
    def calc(self):
        if len(self.text) == 0:
            print 'No text set'
            
        words = nltk.tokenize
        
    
    