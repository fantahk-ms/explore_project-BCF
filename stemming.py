from nltk import tokenize
from nltk.stem import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer

#file=open("sdfklnkncn.txt")
#file.read()
porter=PorterStemmer()

def stemSentence(sentence):
    token_words=word_tokenize(sentence)
    token_words
    stem_sentence=[]
    for word in token_words:
        stem_sentence.append(porter.stem(word))
        stem_sentence.append(" ")
    return "".join(stem_sentence)

#stemSentence(file)

#https://www.datacamp.com/community/tutorials/stemming-lemmatization-python
