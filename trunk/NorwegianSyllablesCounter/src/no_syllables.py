#!/usr/bin/python
# -*- coding: utf-8 -*- 
# Sets the encoding to utf-8 to avoid problems with æøå
import string, re

syllable_path = "files/stavelser"

syllablesInFile = {}

#The last 7, starting at "ai", are the Norwegian diphthongs.
subSyllableIf = ["ges", "ai","au","ei","oy","oi","ui","øy"]
#Tok bort "en$" og "et$"; må forskes mer på.


#Syllables who are not counted as one, but should be.
#Between two vowels that do not form a diphthong.
addSyllableIf = ["oa", "io", "eo", "ia"]

# Compile the regular expressions in aubSyllableIf
for i in range(len(subSyllableIf)):
    subSyllableIf[i] = re.compile(subSyllableIf[i])
for i in range(len(addSyllableIf)):
    addSyllableIf[i] = re.compile(addSyllableIf[i])

def _stripWord(word):
    return word.strip().lower()

# Read our syllable override file and add to the syllablesInFile list
in_syll = open(syllable_path)
for line in in_syll.xreadlines():
    line = line.strip()
    if line:
        toks = line.split()
        assert len(toks) == 2
        syllablesInFile[_stripWord(toks[0])] = int(toks[1])
in_syll.close()

def countNorwegianSyllables(word):

    word = _stripWord(word)

    if not word:
        return 0

    # Check for a cached syllable count
    count = syllablesInFile.get(word, -1)
    
    if count > 0:
        return count

    # Count vowel groups
    count = 0
    prev_was_vowel = 0
    for c in word:
        is_vowel = c in ("a", "e", "i", "o", "u", "y", "æ", "ø", "å")
        if is_vowel and not prev_was_vowel:
            count += 1
        prev_was_vowel = is_vowel

    # Add & subtract syllables
    for r in addSyllableIf:
        if r.search(word):
            count += 1
    for r in subSyllableIf:
        if r.search(word):
            count -= 1

    # Cache the syllable count
    syllablesInFile[word] = count
    
    #Add syllable to file
    file = open(syllable_path, "a")
    file.write(word + " " + str(count) + "\n")
    file.close()

    return count
