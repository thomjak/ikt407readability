from textanalyzer import *

def ARI(text=''):
    score = 0.0
    words = textanalyzer.getWords(text)
    sentences = textanalyzer.getSentences(text)
    totalChars = 0.0
    
    for word in words:
        totalChars += len(word)
    
    totalWords = float(len(words))
    totalSentences = float(len(sentences))
    
    
    print "Words: \t\t" + str(len(words))
    print "Sentences: \t" + str(len(sentences))
    print "Chars: \t\t" + str(totalChars)
    print "syllables: \t" + str(textanalyzer.countSyllables(words))
    
    score = 4.71 * (totalChars / totalWords) + 0.5 * (totalWords / totalSentences) - 21.43
    return score

def FleschReadingEase(text=''):
    score = 0.0
    words = textanalyzer.getWords(text)
    sentences = textanalyzer.getSentences(text)
    
    totalWords = float(len(words))
    totalSentences = float(len(sentences))
    totalSyllables = float(textanalyzer.countSyllables(words))
    
    score = 206.835 - 1.015 * (totalWords / totalSentences) - 84.6 * (totalSyllables / totalWords)
    return score

def FleschKincaidGradeLevel(text=''):
    score = 0.0
    words = textanalyzer.getWords(text)
    sentences = textanalyzer.getSentences(text)
    
    totalWords = float(len(words))
    totalSentences = float(len(sentences))
    totalSyllables = float(textanalyzer.countSyllables(words))
    
    score = 0.39 * (totalWords / totalSentences) + 11.8 * (totalSyllables/totalWords) - 15.59
    return score

    
    
    