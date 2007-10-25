#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import nltk
from textanalyzer import *
import readabilitytests

#print nltk.corpus.brown.words()

text = """
Welcome to Disney Channel, please explore the site to find out
about the great shows on Disney Channel. Why not check out the
TV guide to find out what's on, or see what great prizes can be
won in competitions. You might also want to look at younger
childrens programmes on Playhouse Disney, or see classic episodes
on Toon Disney.
"""
words = textanalyzer.getWords(text)
print "Words: " + str(words)
print "Sentences: " + str(textanalyzer.getSentences(text))
print "Syllables: " + str(textanalyzer.countSyllables(text))
print "Complex words: " + str(textanalyzer.countComplexWords(text))
print "/\\" * 50

print "Flesch Reading Ease: " + str(readabilitytests.FleschReadingEase(text))

print "Flesch-Kincaid Grade Level: " + str(readabilitytests.FleschKincaidGradeLevel(text))

                                  
