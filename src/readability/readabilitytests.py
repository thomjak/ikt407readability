from textanalyzer import *
import math

def ARI(text=''):
    score = 0.0
    words = textanalyzer.getWords(text)
    sentences = textanalyzer.getSentences(text)
    
    totalChars = textanalyzer.getCharacterCount(words)
    totalWords = float(len(words))
    totalSentences = float(len(sentences))
    
    score = 4.71 * (totalChars / totalWords) + 0.5 * (totalWords / totalSentences) - 21.43
    return score

def FleschReadingEase(text=''):
    score = 0.0
    words = textanalyzer.getWords(text)
    sentences = textanalyzer.getSentences(text)
    
    totalWords = float(len(words))
    totalSentences = float(len(sentences))
    totalSyllables = float(textanalyzer.countSyllables(words))
    
    score = 206.835 - 1.015 * (totalWords / totalSentences) - 84.6 * (totalSyllables/ totalWords)
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

def GunningFogIndex(text=''):
    score = 0.0
    words = textanalyzer.getWords(text)
    sentences = textanalyzer.getSentences(text)
    
    totalWords = float(len(words))
    totalSentences = float(len(sentences))
    avgSentenceLength = float(totalWords/totalSentences)
    totalSyllables = float(textanalyzer.countSyllables(words))
    totalComplexWords = float(textanalyzer.countComplexWords(text))
    score = 0.4 * ((avgSentenceLength) + (100 * (totalComplexWords/totalWords)))
    return score

def SMOGIndex(text=''):
    score = 0.0
    sentences = textanalyzer.getSentences(text)
    totalSentences = float(len(sentences))
    totalComplexWords = float(textanalyzer.countComplexWords(text))
    
    score = (math.sqrt(totalComplexWords*(30/totalSentences)) + 3)
    return score

def ColemanLiauIndex(text=''):
    score = 0.0
    words = textanalyzer.getWords(text)
    sentences = textanalyzer.getSentences(text)
    totalChars = textanalyzer.getCharacterCount(words)
    totalWords = float(len(words))
    totalSentences = float(len(sentences))
    
    score = (5.89*(totalChars/totalWords))-(30*(totalSentences/totalWords))-15.8
    return score

def getReportAll(text=''):
    ari = 0.0
    fleschEase = 0.0
    fleschGrade = 0.0
    gunningFog = 0.0
    smog = 0.0
    coleman = 0.0
    
    ari = ARI(text)
    fleschEase = FleschReadingEase(text)
    fleschGrade = FleschKincaidGradeLevel(text)
    gunningFog = GunningFogIndex(text)
    smog = SMOGIndex(text)
    coleman = ColemanLiauIndex(text)
    
    print '*' * 70
    print ' ARI: ' + str(ari)
    print ' Flesch Reading Ease: ' + str(fleschEase)
    print ' FleschKincaid Grade Level: ' + str(fleschGrade)
    print ' Gunning Fog: ' + str(gunningFog)
    print ' SMOG Index: ' + str(smog)
    print ' Coleman-Liau Index: ' + str(coleman)
    print '*' * 70
 
 
 
 
 
 
 
 
 
 
 
 
    
    
    
    