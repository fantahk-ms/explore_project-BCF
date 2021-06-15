#	* Stop words removal, which are common words 
#	(a, the, not, etc) that bring close to no contribution 
#	to the semantic meaning of a text
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
from nltk.tokenize import word_tokenize
import transform

current_list = transform.data_list

#print(stopwords.words('english'))
doc = current_list
tokens = word_tokenize(doc)
filtered_text = [t for t in tokens if not t in stopwords.words("english")]
print(" ".join(filtered_text)) 