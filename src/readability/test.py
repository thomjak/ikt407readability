import nltk
import syllables

print nltk.corpus.brown.words()


word = "Language"
ord = syllables.count_word_fallback(word)
print ord
