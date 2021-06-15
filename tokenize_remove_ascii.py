# import nltk
import transform
import string
from nltk import word_tokenize
# from english_words import english_words_set
# import re

# nltk.download('words')


current_list = transform.data_list
curr = [str(e) for e in current_list ]
ascii_set = set(string.printable)
# words = set(nltk.corpus.words.words())
# d = english_words_set


example = ['Mary had a little lamb' , 
           'Jack went up the hill' , 
           'Jill followed suit' ,'i woke up suddenly' ,
           'it was a really bad dream...', '通过代理上限MDATP设备状态异常 通过代理上限MDATP设备状态异常 apple banana 1234']

# def remove_non_english(data):
    # words = set(nltk.corpus.words.words())
    # for i in data:
        # if i.lower() not in d:
            # data.remove(i)
    # data = list(filter(lambda ele: re.search("[a-zA-Z\s]+", ele) is not None, data))
  
            

def remove_non_ascii(data):
    return [word for word in data 
        if all(char in ascii_set for char in word)]


def tokenize(data):
  tokenized_sents = [word_tokenize(i) for i in data]


tokenize(curr)

# remove_non_english(example)
# print(curr)

curr = remove_non_ascii(curr)
print(curr)