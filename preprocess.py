from pickle import TRUE

from numpy import empty
import transform
import string
import nltk
from nltk.corpus import stopwords
# nltk.download('stopwords')
# nltk.download('punkt')
from nltk import word_tokenize
import re
from nltk import tokenize
# from nltk.stem import sent_tokenize
from nltk.stem import PorterStemmer 
import pandas as pd

current_list = transform.support_list
curr = list(map(str, current_list))

process_df = transform.df_process
process_list = transform.process_list
process = list(map(str, process_list))
tickets = process_df['Ticket']
platforms = process_df['Platform']
subgroups = process_df['Category']

tickets1 = tickets.tolist()
new_tickets = list(map(str, tickets1))




ascii_set = set(string.printable)
porter=PorterStemmer()
exclusion_list = ['grand', 'total','none', 'hello','hi','team','how','i','\\n','please', 'pii', 'defender', 'microsoft', 'endpoint', 'thanks', 'monday', 'tuesday', 
'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'ticket', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
stemmed_exclusion_list = [porter.stem(y) for y in exclusion_list]


# ask xinny for list of "bad words" --> pii, microsoft, defend
# add method to weed out short titles/descriptions


example = ['Hi team, Mary had a the that [little] lamb None{} defender' , 
           'Jack went up the has hill himself Grand Total?' , 
           'Jill followed all she_! suit Please' ,'i woke up suddenly pii' ,
           'it was a really bad defend pii own more $%*dream..\\n.', '通过代理上限MDATP设备状态异常 通过代理上限MDATP设备状态异常 apple banana 1234', 'None', 'None Grand Total', 
           'Pythoners are very intelligent and work very pythonly and now they are pythoning their way to success.']

def remove_non_ascii(data):
    return [word for word in data 
        if all(char in ascii_set for char in word)]


def tokenize(data):
  tokenized_sents = [word_tokenize(i) for i in data]
  data = tokenized_sents
 # return data

def remove_extra(data):
  # remove_list = [porter.stem(y) for y in badwords]
  print(stemmed_exclusion_list)
   # extra = ['None', 'Grand', 'Total']
  tokens = [word_tokenize(i) for i in data]
  # tokens = [porter.stem(x) for x in tokens]
  #  filtered = []
  for i in range(len(tokens)):
       # check to see what bad words are stemmed, stem first, then run through bad words
       # tokens = [porter.stem(x) for x in tokens[i]]
       # filtered = [porter.stem(x) for x in tokens[i]]
       #print(filtered)
       filtered = [t for t in tokens[i] if t.isalpha() and not t.lower() in exclusion_list + stopwords.words("english")]
       #print(filtered)
       filtered = [porter.stem(x) for x in filtered if not x in stemmed_exclusion_list]
       #print(filtered)
       # filtered = [t for t in tokens[i] if t.isalpha() and not t.lower() in badwords + stopwords.words("english")]
       # print(*filtered)
       data[i] = " ".join(filtered)
      # print("\n")
   # return filtered
  # for i in data:
      # filtered = [t for t in i if t.isalpha() and not t.lower() in badwords + stopwords.words("english")]


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


# new_ex = [str(e) for e in example ]

# curr = list(map(str, example))


#for i in range(len(process)):
 #   tokenize(process[i][2])
  #  process[i][2] = remove_non_ascii(process[i][2])
   # remove_extra(process[i][2])
    #if (process[i][2] is empty):
     #   process.remove(process[i])
#print(process)
    



tokenize(process_df['Ticket'])

process_df.dropna(subset=["Ticket"], inplace=True)


process_df['Ticket'] = remove_non_ascii(process_df['Ticket'])


remove_extra(process_df['Ticket'])




#df = pd.DataFrame(process_df)

print(process_df)

#df.dropna(subset=["Ticket"], inplace=True)

print(process_df['Ticket'])


#ser = pd.Series(new_tickets)
#print(ser)
#process_df["Ticket"] = ser

#print(process_df['Ticket'])
#print(process_df)

#to_export = process_df.to_csv(r'/Users/t-fkabba/Downloads/PreProcessed4.csv', index=False)

