#!/usr/bin/python
# -*- coding: utf-8 -*- 
# Sets the encoding to utf-8 to avoid problems with æøå

import nltk
from textanalyzer import *
from languageclassifier import *
from readabilitytests import ReadabilityTool
from urlextracter import *
from textanalyzer import *


#print "Using URL as input"
#print "*" * 40
ue = URLextracter("http://www.openbsd.org/cgi-bin/man.cgi?query=ssh")
#print "Number of links: %s" % len(ue.linklist)
text = ue.output()
#nb = NaiveBayes()
#nb.train("/home/thomas/mined2")
#nb.testAccuracy(nb.test_files)
#print "Lang: %s" % nb.classifyText(text)
#textanalyzer.analyzeText(text)

URLextracter.demo()
textanalyzer.demo()
ReadabilityTool.demo()
