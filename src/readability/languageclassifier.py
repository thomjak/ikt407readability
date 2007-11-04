from nltk.corpus import stopwords

import glob
import random
import math
import pickle

from urlextracter import URLextracter
from sgmllib import *

class NaiveBayes():
       
    def __init__(self):
        self.nor_stopwords = {}
        for word in stopwords.words('norwegian'):
            self.nor_stopwords[word] = True
            
        self.eng_stopwords = {}
        for word in stopwords.words('english'):
            self.eng_stopwords[word] = True
            
    def load(self,picklepath):
        p = open(picklepath, 'r')
        p_word_given_lang = pickle.load(p)
        self.p_word_given_lang = p_word_given_lang
        
        
        
    def train(self, path):
        # Setup
        print "Training started..."
        training_files = glob.glob(path + "/*/*")
        random.shuffle(training_files)
        
        self.files = {}
        self.p_lang = {}
        
        # Calculate P(H)
        for file in training_files[0:200]:
            values = file.split('/')
            lang = values[-2]
        
            if not self.p_lang.has_key(lang):
                self.p_lang[lang] = 0.0
            
            self.p_lang[lang] += 1.0
            
            if not self.files.has_key(lang):
                self.files[lang] = []
            
            f = open(file, 'r')
            self.files[lang] += f.read().replace("\n", " ").replace(".", "").split(" ")
            f.close()
            
        # Calculate probabilities
        for lang in self.p_lang.keys():
            self.p_lang[lang] /= len(training_files)
            
        self.vocabulary = self.__createVocabulary(self.files)
        
        # Calculate P(O | H) 
        p_word_given_lang = self.p_word_given_lang
        for lang in self.files.keys():
            p_word_given_lang[lang] = {}
            
            for word in self.vocabulary.keys():
                p_word_given_lang[lang][word] = 1.0
            
            for word in self.files[lang]:
                if self.vocabulary.has_key(word):
                    p_word_given_lang[lang][word] += 1.0
                    
            for word in self.vocabulary.keys():
                p_word_given_lang[lang][word] /= len(self.files[lang]) + len(self.vocabulary)
                
        print "Training finished..."
        
        # Save result as a file
        output = open("/home/thomas/test.pickle",'w')
        pickler = pickle.dump(p_word_given_lang, output, -1)
        output.close()   
        
    def __createVocabulary(self, files):
        # Count number of occurance of each word
        word_count = {}
        for lang in files.keys():
            for word in files[lang]:
                if not word_count.has_key(word):
                    word_count[word] = 0
                word_count[word] += 1
        
        vocabulary = {}
        for word in word_count.keys():
            if word_count[word] > 2 and not self.nor_stopwords.has_key(word) and not self.eng_stopwords.has_key(word):
                if word != '':
                    vocabulary[word] = True
                
        return vocabulary
    
    def testAccuracy(self,path):
        errors = 0.0
        total = 0.0
        
        test_files = glob.glob(path + "/*/*")
        random.shuffle(test_files)
        
        
        for file in test_files[201:]:
            values = file.split("/")
            true_lang = values[-2]

            f = open(file, "r")    
            file_to_be_classified = f.read().replace("\n", " ").replace(".", "").split(" ")
            f.close()
            
            # Finds group with max P(O | H) * P(H)
            max_lang = 0
            max_p = 1
            for candidate_lang in self.files.keys():
                # Calculates P(O | H) * P(H) for candidate group
                p = math.log(self.p_lang[candidate_lang])
                for word in file_to_be_classified:
                    if self.vocabulary.has_key(word):
                        p += math.log(self.p_word_given_lang[candidate_lang][word])
        
                if p > max_p or max_p == 1:
                    max_p = p
                    max_lang = candidate_lang
        
            total += 1.0
            if true_lang != max_lang:
                errors += 1.0
                
        print "Accuracy: %.3f" % (1.0 - errors/total)
    
    def classifyText(self, text):
        max_lang = 0
        max_p = 1
        for candidate_lang in self.files.keys():
            # Calculates P(O | H) * P(H) for candidate group
            p = math.log(self.p_lang[candidate_lang])
            for word in text.split(' '):
                if self.vocabulary.has_key(word):
                    p += math.log(self.p_word_given_lang[candidate_lang][word])
    
            if p > max_p or max_p == 1:
                max_p = p
                max_lang = candidate_lang
        
        print "Language of text is: " + max_lang
    
    def classifyURL(self, url):
        ue = URLextracter(url)
        print 'Language of URL '
        self.classifyText(ue.output())
    
    def handle_decl(self,data):
        pass

    def report_unbalanced(self,tag):
        pass
    
if __name__=="__main__":
    nb = NaiveBayes()
    nb.load("/home/thomas/test.pickle")
    nb.train("/home/thomas/mined")
    nb.testAccuracy("/home/thomas/mined")
    nb.classifyURL("http://www.woman24.no")
    