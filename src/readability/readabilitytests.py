from textanalyzer import *
import math

analyzedVariables = {}

def getTextVariables(text = ''):
    words = textanalyzer.getWords(text)
    charCount = textanalyzer.getCharacterCount(words)
    wordCount = len(words)
    sentenceCount = len(textanalyzer.getSentences(text))
    syllableCount = textanalyzer.countSyllables(words)
    complexwordsCount = textanalyzer.countComplexWords(text)
    averageWordsPerSentence = wordCount/sentenceCount
    
    analyzedVariables['charCount'] = float(charCount)
    analyzedVariables['wordCount'] = float(wordCount)
    analyzedVariables['sentenceCount'] = float(sentenceCount)
    analyzedVariables['syllableCount'] = float(syllableCount)
    analyzedVariables['complexwordCount'] = float(complexwordsCount)
    analyzedVariables['averageWordsPerSentence'] = float(averageWordsPerSentence)
    
def CalculateAllTests(text = ''):
    getTextVariables(text)
    getReportAll()
 

def ARI():
    score = 0.0
    
    score = 4.71 * (analyzedVariables['charCount'] / analyzedVariables['wordCount']) + 0.5 * (analyzedVariables['wordCount'] / analyzedVariables['sentenceCount']) - 21.43
    return score

def FleschReadingEase():
    score = 0.0
    
    score = 206.835 - (1.015 * (analyzedVariables['averageWordsPerSentence'])) - (84.6 * (analyzedVariables['syllableCount']/ analyzedVariables['wordCount']))
    return score

def FleschKincaidGradeLevel():
    score = 0.0

    score = 0.39 * (analyzedVariables['averageWordsPerSentence']) + 11.8 * (analyzedVariables['syllableCount']/ analyzedVariables['wordCount']) - 15.59
    return score

def GunningFogIndex():
    score = 0.0
   
    score = 0.4 * ((analyzedVariables['averageWordsPerSentence']) + (100 * (analyzedVariables['complexwordCount']/analyzedVariables['wordCount'])))
    return score

def SMOGIndex():
    score = 0.0
    
    score = (math.sqrt(analyzedVariables['complexwordCount']*(30/analyzedVariables['sentenceCount'])) + 3)
    return score

def ColemanLiauIndex():
    score = 0.0
    
    score = (5.89*(analyzedVariables['charCount']/analyzedVariables['wordCount']))-(30*(analyzedVariables['sentenceCount']/analyzedVariables['wordCount']))-15.8
    return score

def getReportAll():
    ari = 0.0
    fleschEase = 0.0
    fleschGrade = 0.0
    gunningFog = 0.0
    smog = 0.0
    coleman = 0.0
    
    ari = ARI()
    fleschEase = FleschReadingEase()
    fleschGrade = FleschKincaidGradeLevel()
    gunningFog = GunningFogIndex()
    smog = SMOGIndex()
    coleman = ColemanLiauIndex()
    
    print '*' * 70
    print ' ARI: %.1f' % ari
    print ' Flesch Reading Ease: %.1f' % fleschEase
    print ' FleschKincaid Grade Level: %.1f' % fleschGrade
    print ' Gunning Fog: %.1f' % gunningFog
    print ' SMOG Index: %.1f' % smog
    print ' Coleman-Liau Index: %.1f' % coleman
    print '*' * 70
 
 
 
 
 
 
 
 
 
 
 
 
    
    
    
    