import nltk

sentence = "NLTK is a leading platform for building Python programs to work with human language data."

tokens = nltk.word_tokenize(sentence)
print(tokens)

tagged = nltk.pos_tag(tokens)
print(tagged)
