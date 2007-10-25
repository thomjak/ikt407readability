import nltk
from textanalyzer import *

import readabilitytests

#text = ("Good muffins cost $3.88\nin New York.  Please buy me\ntwo of them.\n\nThanks.")
text = """
This is an interactive web page for checking a sample of writing. 
It is modeled after the ancient Unix utilities style and diction. 
Enter or copy text into the first box below. The scores to the 
right give the readability of the text according to various formulas.
"""
words = textanalyzer.getWords(text)
print "words: " + str(words)
print "sentences: " + str(textanalyzer.getSentences(text))
print "=" * 100

print "ARI: " + str(readabilitytests.ARI(text))

print "Flesch Reading Ease : " + str(readabilitytests.FleschReadingEase(text))