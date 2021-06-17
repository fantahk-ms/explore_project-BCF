# import nltk
import transform
import string
from nltk import word_tokenize
import re
# from english_words import english_words_set
# import re

# nltk.download('words')


current_list = transform.data_list
curr = [str(e) for e in current_list ]
ascii_set = set(string.printable)
# ascii_set = set(r'[\W_]+')
# words = set(nltk.corpus.words.words())
# d = english_words_set


example = ['Mary had a little lamb *** None' , 
           'Jack went up the hill $#! Grand Total' , 
           'Jill followed suit)*' ,'i woke^& up suddenly' ,
           'it was a really bad dream...', '通过代理上限MDATP设备状态异常 通过代理上限MDATP设备状态异常 apple banana 1234', 'None', 'None Grand Total', '!@#$']

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
  data = tokenized_sents
 # return data

def remove_extra(data):
   # extra = ['None', 'Grand', 'Total']
   tokens = [word_tokenize(i) for i in data]
  #  filtered = []
   for i in range(len(tokens)):
       filtered = [t for t in tokens[i] if t.isalpha() and not t in extra]
       # print(*filtered)
       data[i] = filtered   
      # print("\n")
   # return filtered


# def remove_nonwords(data):
    # data = [str(x) for x in data]
    # tokens = [word_tokenize(i) for i in data]
    #for i in range(len(tokens)):
        #y = str(tokens[i])
        #re.sub(r'[\W_]+', ' ', y)
    
    


tokenize(example)

# remove_extra(curr)
# print(curr)

# remove_extra(example)
example = remove_non_ascii(example)
remove_extra(example)
# remove_non_number_words(example)
print(example)

# try switching order
# try moving it into remove_ascii