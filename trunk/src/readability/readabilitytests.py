from textanalyzer import *

def ARI(text=''):
    value = 0
    words = textanalyzer.getWords(text)
    sentences = textanalyzer.getSentences(text)
    totalchars = 0
    
    for word in words:
        totalchars += len(word)
    
    print 'Words: ' + str(len(words)) + " Sentences: " + str(len(sentences))
    print 'Chars: ' + str(totalchars)
    
    value = 4.71 * (totalchars / len(words)) + 0.5 * (len(words) / len(sentences)) - 21.43
    return value