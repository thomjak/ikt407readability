#!/usr/bin/python
# -*- coding: UTF-8 -*-

import nltk
from textanalyzer import *
import readabilitytests

#print nltk.corpus.brown.words()

#text = """
#Welcome to Disney Channel, please explore the site to find out
#about the great shows on Disney Channel. Why not check out the
#TV guide to find out what's on, or see what great prizes can be
#won in competitions. You might also want to look at younger
#childrens programmes on Playhouse Disney, or see classic episodes
#on Toon Disney.
#"""

text = """
The wizarding world in which Harry finds himself is both completely separate from and yet intimately connected to our own world. While the fantasy world of Narnia is an alternative universe and the Lord of the Rings’ Middle-earth a mythic past, the wizarding world of Harry Potter exists alongside ours and contains magical elements analogous to things in the non-magical world. Many of its institutions and locations are in towns and cities, including London for example, that are recognisable in the real world. It possesses a fragmented collection of hidden streets, overlooked and ancient pubs, lonely country manors and secluded castles that remain invisible to the non-magical population (known as "Muggles"; e.g., The Dursleys). Wizard ability is inborn, rather than learned, although one must attend schools such as Hogwarts in order to master and control it. However it is possible for wizard parents to have children who are born with little or no magical ability at all (known as "Squibs"; e.g., Mrs. Figg, Argus Filch). Since one is either born a wizard or not, most wizards are unfamiliar with the Muggle world, which appears stranger to them than their world does to us. The magical world and its many fantastic elements are depicted in a matter-of-fact way. This juxtaposition of the magical and the mundane is one of the principal motifs in the novels; the characters in the stories live normal lives with normal problems, for all their magical surroundings.
"""

words = textanalyzer.getWords(text)
print "Words: " + str(words)
print "Sentences: " + str(textanalyzer.getSentences(text))
print "Syllables: " + str(textanalyzer.countSyllables(text))
print "Complex words: " + str(textanalyzer.countComplexWords(text))
print "/\\" * 50

readabilitytests.getReportAll(text)
                                  
