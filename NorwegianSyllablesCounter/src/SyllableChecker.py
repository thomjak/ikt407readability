
import os


syllable_path = os.path.join("files", "stavelser")
syllables = open(syllable_path)

newsyllable_path = os.path.join("files", "correctsyllables")
newSylls = open(newsyllable_path, "a")

for syllable in syllables.xreadlines():
    syllable = syllable.strip()
    if syllable:
        toks = syllable.split()
        assert len(toks) == 2
        print "Har '" + toks[0] + "' - " + toks[1] + " syllables?"
        answer = raw_input("(enter or new number of syllables) > ")
        print answer
        if answer == "\r":
           continue
        elif  answer == "q\r":
            break
        else:
           newSylls.write(toks[0] + " " + str(answer))
           newSylls.flush()          
           print "\nLagret..."
           
           
syllables.close()
newSylls.close()
