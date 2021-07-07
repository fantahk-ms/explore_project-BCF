import transform
import preprocess
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from nltk.tokenize.treebank import TreebankWordDetokenizer
from collections import Counter
import numpy as np
import ast

# importing
# cluster_df = transform.df_cluster
cluster_list = transform.cluster_list

# convert to list
print("here, line 16")
# curr = [str(e) for e in cluster_list ]
print("here, line 18")

#example to run on
example = ["Cricket is a bat and ball game played between two teams of eleven players each on a cricket field.", 
    "Each phase of play is called an innings during which one team bats, attempting to score as many runs as possible.", 
    "The teams have one or two innings apiece and, when the first innings ends, the teams swap roles for the next innings",
    "Before a match begins, the two team captains meet on the pitch for the toss of a coin to determine which team will bat first.", 
    "Two batsmen and eleven fielders then enter the field and play begins when a member of the fielding team, known as the bowler, delivers the ball.", 
    "The most common dismissal in cricket match are bowled, when the bowler hits the stumps directly with the ball and dislodges the bails. Batsman gets out.", 
    "Runs are scored by two main methods: either by hitting the ball hard enough for it to cross the boundary, or by the two batsmen swapping ends.", 
    "The main objective of each team is to score more runs than their opponents.", 
    "If the team batting last is all out having scored fewer runs than their opponents, they are said to have 'lost by n runs'.", 
    "The role of striker batsman is to prevent the ball from hitting the stumps by using his bat and, simultaneously, to strike it well enough to score runs", 
    "Artificial intelligence is intelligence exhibited by machines, rather than humans or other animals.",  
    "the field of AI research defines itself as the study of 'intelligent agents': any device that perceives its environment and takes actions that maximize its chance of success at some goal", 
    "The overall research goal of artificial intelligence is to create technology that allows computers and machines to function in an intelligent manner.", 
    "Natural language processing[77] gives machines the ability to read and understand human language and extract intelligence from it.", 
    "AI researchers developed sophisticated mathematical tools to solve specific subproblems. These tools are truly scientific, in the sense that their results are both measurable and verifiable.", 
    "An intelligent agent is a system that perceives its environment and takes actions which maximize its chances of success.", 
    "AI techniques have become an essential part of the technology industry, helping to solve many challenging problems in computer science.", 
    "Recent advancements in AI, and specifically in machine learning, have contributed to the growth of Autonomous Things such as drones and self-driving cars.", 
    "AI research was revived by the commercial success of expert systems,[28] a form of AI program that simulated the knowledge and analytical skills of human experts.", 
    "Advanced statistical techniques (loosely known as deep learning), access to large amounts of data and faster computers enabled advances in machine learning and perception.", 
    "A compound is a pure chemical substance composed of more than one element and the properties of a compound bear little similarity to those of its elements.", 
    "Since the properties of an element are mostly determined by its electron configuration, the properties of the elements likewise show recurring patterns or periodic behaviour.", 
    "The property of inertness of noble gases makes them very suitable in chemicals where reactions are not wanted.", 
    "The atom is also the smallest entity that can be envisaged to retain the chemical properties of the element, such as electronegativity, ionization potential and preferred oxidation state.", 
    "The nucleus is made up of positively charged protons and uncharged neutrons (together called nucleons), while the electron cloud consists of negatively charged electrons which orbit the nucleus", 
    "The atom is the basic unit of chemistry. It consists of a dense core called the atomic nucleus surrounded by a space called the electron cloud.", 
    "A chemical reaction is a transformation of some substances into one or more different substances.", 
    "Chemistry is sometimes called the central science because it bridges other natural sciences, including physics, geology and biology.", 
    "Chemistry includes topics such as the properties of individual atoms and how atoms form chemical bonds to create chemical compounds.", 
    "Chemistry is a branch of physical science that studies the composition, structure of atoms, properties and change of matter."]


test_sentences = ['Chemical compunds are used for preparing bombs based on some reactions', 
'Cricket is a boring game where the batsman only enjoys the game', 
'Machine learning is a area of Artificial intelligence']


# pre-processing
#preprocess.tokenize(example)
#example = preprocess.remove_non_ascii(example)
#preprocess.remove_extra(example)
#example = preprocess.stemSentence(example)

#turning list into actual list
#example = ast.literal_eval(example)


# testing sentences pre-processing
#preprocess.tokenize(test_sentences)
#test_sentences = preprocess.remove_non_ascii(test_sentences)
#preprocess.remove_extra(test_sentences)
#test_sentences = preprocess.stemSentence(test_sentences)

#turning list into actual list
#test_sentences = ast.literal_eval(test_sentences)

curr = [str(e) for e in cluster_list ]


# pre-processing
#print("here, before pre-processing")
preprocess.tokenize(curr)
#print("here, after tokenize")
curr = preprocess.remove_non_ascii(curr)
#print("here, after remove non-ascii")
preprocess.remove_extra(curr)
#print("here, after remove extra")
#curr = preprocess.stemSentence(curr)
#print("here, after stem sentence")


#print("here, after pre-processing")

#print("here, before list transform")
#turning list into actual list
# curr = ast.literal_eval(curr)
#print("here, after list transform")


#print(cluster_list)




#vectorization
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(curr)

# clustering
k = 30
model = KMeans(n_clusters=k, init='k-means++', max_iter=200, n_init=1)
model.fit(X)

#test sentences vectorization
#test = vectorizer.transform(test_sentences)

# test sentences prediction
#predicted_labels_kmeans = model.predict(test)


# top terms printed out
print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(k):
    print("Cluster %d:" % i),
    for ind in order_centroids[i, :20]:
        print(' %s' % terms[ind]),
    print

print("\n")


# test
#print("\n-------------------------------PREDICTIONS BY K-Means--------------------------------------")
#print("\nIndex of Cricket cluster : ",Counter(model.labels_[0:10]).most_common(1)[0][0])
#print("Index of Artificial Intelligence cluster : ",Counter(model.labels_[10:20]).most_common(1)[0][0])
#print("Index of Chemistry cluster : ",Counter(model.labels_[20:30]).most_common(1)[0][0])
 
#print("\n",test_sentences[0],":",predicted_labels_kmeans[0],\
#"\n",test_sentences[1],":",predicted_labels_kmeans[1],\
#"\n",test_sentences[2],":",predicted_labels_kmeans[2])







