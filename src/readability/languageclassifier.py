#!/usr/bin/python
# -*- coding: utf-8 -*- 
# Sets the encoding to utf-8 to avoid problems with æøå
from nltk.corpus import stopwords

import glob
import re
import random
import math
import pickle

from urlextracter import URLextracter
from sgmllib import *

class NaiveBayes():
       
    p_word_given_lang = {}
    
    training_files = []
    test_files = []

    def __init__(self):
        self.nor_stopwords = {}
        for word in stopwords.words('norwegian'):
            self.nor_stopwords[word] = True
            
        self.eng_stopwords = {}
        for word in stopwords.words('english'):
            self.eng_stopwords[word] = True
            
        self.load("/home/thomas/test.pickle")    # CHANGE THIS

            
    def load(self,picklepath):
        try:
            p = open(picklepath, 'r')
            self.p_word_given_lang = pickle.load(p)
        except IOError:
            self.p_word_given_lang = {}
            print "Nothing to load here!"
        
        
        
    def train(self, path):
        # Setup
        data_files = glob.glob(path + "/*/*")
        random.shuffle(data_files)
        
        self.training_files = data_files[0:300]
        self.test_files = data_files[300:400]
        
        self.files = {}
        self.p_lang = {}
        
        # Calculate P(H)
        for file in self.training_files:
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
            self.p_lang[lang] /= len(self.training_files)
            
        self.vocabulary = self.__createVocabulary(self.files)
        
        # Calculate P(O | H) 
        p_word_given_lang = self.p_word_given_lang
        for lang in self.files.keys():
            p_word_given_lang[lang] = {}
            
            for word in self.vocabulary[lang].keys():
                p_word_given_lang[lang][word] = 1.0
            
            for word in self.files[lang]:
                if self.vocabulary[lang].has_key(word):
                    p_word_given_lang[lang][word] += 1.0
                    
            for word in self.vocabulary[lang].keys():
                p_word_given_lang[lang][word] /= len(self.files[lang]) + len(self.vocabulary[lang])
                
        print "Training finished...(training-set of size %d)" % len(self.training_files)
        self.p_word_given_lang = p_word_given_lang
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
        vocabulary['eng'] = {}
        vocabulary['no'] = {}
        for word in word_count.keys():
            if word_count[word] > 2:
                if word != '':
                    if not word in self.nor_stopwords:
                        vocabulary['no'][word] = True
                    if not word in self.eng_stopwords:
                        vocabulary['eng'][word] = True
        return vocabulary
    
    def testAccuracy(self,test_files):
        errors = 0.0
        total = 0.0
        
        # Use if test_files is provided as path
        #test_files = glob.glob(path + "/*/*")
        #random.shuffle(test_files)
        
        
        for file in self.test_files:
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
                    if self.vocabulary[candidate_lang].has_key(word):
                        p += math.log(self.p_word_given_lang[candidate_lang][word])
        
                if p > max_p or max_p == 1:
                    max_p = p
                    max_lang = candidate_lang
        
            total += 1.0
            if true_lang != max_lang:
                errors += 1.0
        print "Classifying finished...(test-set of size %d)" % len(self.test_files)
        print "Errors %d" % errors
        print "Total %d" % total
        print "Accuracy: %.3f" % (1.0 - errors/total)
    
    def classifyText(self, text):
        max_lang = 0
        max_p = 1
        for candidate_lang in self.files.keys():
            # Calculates P(O | H) * P(H) for candidate group
            p = math.log(self.p_lang[candidate_lang])
            for word in text.split(' '):
                if self.vocabulary[candidate_lang].has_key(word):
                    p += math.log(self.p_word_given_lang[candidate_lang][word])
    
            if p > max_p or max_p == 1:
                max_p = p
                max_lang = candidate_lang
        
        return max_lang
    
    def classifyURL(self, url):
        ue = URLextracter(url)
        print 'Classifying %s' % url
        content = ue.output() 
        content = re.sub(r"[^a-zA-ZæøåÆØÅ]", " ", content)
        content = content.strip()
        return self.classifyText(content)
    
    def handle_decl(self,data):
        pass

    def report_unbalanced(self,tag):
        pass
    
if __name__=="__main__":
    import os
    os.system("clear")
    print "Demo of languageclassifier.py"
    print "=" * 40
    nb = NaiveBayes()
    nb.train("/home/thomas/mined2/")
    nb.testAccuracy(nb.test_files)
    print "\n"
    
    lang = nb.classifyURL("http://harvardscience.harvard.edu/")
    print "-->language: %s \n" % lang
    lang = nb.classifyURL("http://vg.no")
    print "-->language: %s \n" % lang
    lang = nb.classifyURL("http://itavisen.no")
    print "-->language: %s \n" % lang
    lang = nb.classifyURL("http://bbc.co.uk")
    print "-->language: %s \n" % lang
    lang = nb.classifyURL("http://startsiden.no")
    print "-->language: %s \n" % lang
    lang = nb.classifyURL("http://news.com")
    print "-->language: %s \n" % lang
    raw_input("I'm done. Press ENTER")
    
    