#   * Stop words removal, which are common words 
#   (a, the, not, etc) that bring close to no contribution 
#   to the semantic meaning of a text
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
from nltk.tokenize import word_tokenize
import transform
import re

current_list = transform.data_list
curr = [str(e) for e in current_list ]
print(stopwords.words('english')) 
print("\n")

example = ['Hi team, Mary had a the that [little] lamb None{}' , 
           'Jack went up the has hill himself Grand Total?' , 
           'Jill followed all she_! suit Please' ,'i woke up suddenly' ,
           'it was a really bad own more $%*dream..\\n.', '通过代理上限MDATP设备状态异常 通过代理上限MDATP设备状态异常 apple banana 1234', 'None', 'None Grand Total']
curr = example   
badwords = ['Grand', 'Total','None', 'Hello','Hi','Team','How','I','\\n','Please']
punctuation = ['!','(',')','-','[',']','{','}',';',':','\\','<','>','.','/','?','@','#','$','%','^','&','*','_','~']

def removestopwords(data):
    tokens = [word_tokenize(i) for i in data]
    for i in range(len(tokens)):
        filtered_text = [t for t in tokens[i] if not t in stopwords.words("english") + badwords + punctuation]
 #add to new list
        print(*filtered_text)
        print("\n")

