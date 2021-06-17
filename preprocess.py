import transform
import string
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
from nltk import word_tokenize
import re
from nltk import tokenize
# from nltk.stem import sent_tokenize
from nltk.stem import PorterStemmer


current_list = transform.data_list
curr = [str(e) for e in current_list ]

ascii_set = set(string.printable)
porter=PorterStemmer()
badwords = ['grand', 'total','none', 'hello','hi','team','how','i','\\n','please']


example = ['Hi team, Mary had a the that [little] lamb None{}' , 
           'Jack went up the has hill himself Grand Total?' , 
           'Jill followed all she_! suit Please' ,'i woke up suddenly' ,
           'it was a really bad own more $%*dream..\\n.', '通过代理上限MDATP设备状态异常 通过代理上限MDATP设备状态异常 apple banana 1234', 'None', 'None Grand Total', 
           'Pythoners are very intelligent and work very pythonly and now they are pythoning their way to success.']

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
       filtered = [t for t in tokens[i] if t.isalpha() and not t.lower() in badwords + stopwords.words("english")]
       # print(*filtered)
       data[i] = filtered   
      # print("\n")
   # return filtered


def stemSentence(sentence):
    sentence = str(sentence)
    token_words=word_tokenize(sentence)
    token_words
    stem_sentence=[]
    for word in token_words:
        stem_sentence.append(porter.stem(word))
        stem_sentence.append(" ")
    return "".join(stem_sentence)
       # "".join(stem_sentence)

def removestopwords(data):
    tokens = [word_tokenize(i) for i in data]
    for i in range(len(tokens)):
        filtered_text = [t for t in tokens[i] if not t in stopwords.words("english")]
        data[i] = filtered_text   

tokenize(curr)

curr = remove_non_ascii(curr)
remove_extra(curr)
# removestopwords(example)

#for i in example:
    #i = stemSentence(i)

curr = stemSentence(curr)

print(curr)

