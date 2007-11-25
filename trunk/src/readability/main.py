#!/usr/bin/python
# -*- coding: utf-8 -*- 
# Sets the encoding to utf-8 to avoid problems with æøå

from languageclassifier import *
from textanalyzer import *
from readabilitytests import *

def getinfo(text):
    lnb = NaiveBayes()
    ta = textanalyzer()
    rt = ReadabilityTool()
    
    lang = lnb.classifyText(text)
    
    print "The language of the text is determined to be:\t%s\n" % lang
    
    print "Text statistics"
    print "=" * 50
    ta.analyzeText(text)
    
    
    print "\nSuggested readabilitytests:"
    print "=" * 50
    print "LIX: %.1f" % rt.LIX(text)
    print "FOG: %.1f" % rt.GunningFogIndex(text)
    



    
getinfo("Howard har vært statsminister i 11 og et halvt år og har vært populær blant folket, noe fire valgseire understreker. Denne gangen risikerer han derimot å miste sitt eget sete i nasjonalforsamlingen etter et katastrofalt dårlig valg, som ga Labour-partiet en seiersmargin på 6,3 prosent.")
    