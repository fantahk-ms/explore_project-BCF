import preprocess
import transform
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

example = ['Cricket is a bat and ball game played between two teams of eleven players each on a cricket field.' , 

'Each phase of play is called an innings during which one team bats, attempting to score as many runs as possible.', 

'The teams have one or two innings apiece and, when the first innings ends, the teams swap roles for the next innings',

 'Before a match begins, the two team captains meet on the pitch for the toss of a coin to determine which team will bat first.', 

 'Two batsmen and eleven fielders then enter the field and play begins when a member of the fielding team, known as the bowler, delivers the ball.', 

 'The most common dismissal in cricket match are bowled, when the bowler hits the stumps directly with the ball and dislodges the bails. Batsman gets out.', 

 'Runs are scored by two main methods: either by hitting the ball hard enough for it to cross the boundary, or by the two batsmen swapping ends.', 

 'The main objective of each team is to score more runs than their opponents.', 

 'If the team batting last is all out having scored fewer runs than their opponents, they are said to have "lost by n runs".', 

 'The role of striker batsman is to prevent the ball from hitting the stumps by using his bat and, simultaneously, to strike it well enough to score runs', 

 'Artificial intelligence is intelligence exhibited by machines, rather than humans or other animals.',  

 'the field of AI research defines itself as the study of "intelligent agents": any device that perceives its environment and takes actions that maximize its chance of success at some goal', 

 'The overall research goal of artificial intelligence is to create technology that allows computers and machines to function in an intelligent manner.', 

 'Natural language processing[77] gives machines the ability to read and understand human language and extract intelligence from it.', 

 'AI researchers developed sophisticated mathematical tools to solve specific subproblems. These tools are truly scientific, in the sense that their results are both measurable and verifiable.', 

 'An intelligent agent is a system that perceives its environment and takes actions which maximize its chances of success.', 

 'AI techniques have become an essential part of the technology industry, helping to solve many challenging problems in computer science.', 

 'Recent advancements in AI, and specifically in machine learning, have contributed to the growth of Autonomous Things such as drones and self-driving cars.', 

 'AI research was revived by the commercial success of expert systems,[28] a form of AI program that simulated the knowledge and analytical skills of human experts.', 

 'Advanced statistical techniques (loosely known as deep learning), access to large amounts of data and faster computers enabled advances in machine learning and perception.', 

 'A compound is a pure chemical substance composed of more than one element and the properties of a compound bear little similarity to those of its elements.', 

 'Since the properties of an element are mostly determined by its electron configuration, the properties of the elements likewise show recurring patterns or periodic behaviour.', 

 'The property of inertness of noble gases makes them very suitable in chemicals where reactions are not wanted.', 

 'The atom is also the smallest entity that can be envisaged to retain the chemical properties of the element, such as electronegativity, ionization potential and preferred oxidation state.', 

 'The nucleus is made up of positively charged protons and uncharged neutrons (together called nucleons), while the electron cloud consists of negatively charged electrons which orbit the nucleus', 

 'The atom is the basic unit of chemistry. It consists of a dense core called the atomic nucleus surrounded by a space called the electron cloud.', 

 'A chemical reaction is a transformation of some substances into one or more different substances.', 

 'Chemistry is sometimes called the central science because it bridges other natural sciences, including physics, geology and biology.', 

 'Chemistry includes topics such as the properties of individual atoms and how atoms form chemical bonds to create chemical compounds.', 

 'Chemistry is a branch of physical science that studies the composition, structure of atoms, properties and change of matter.']

#test_sentences=[preprocess.example]

vectorizer = CountVectorizer()
vectorizer.fit(example)
vector = vectorizer.transform(example)
X=vector.toarray()
print(X)

y = X.iloc[:, 0]
X_train, X_test, y_train, y_test = train_test_split(X, y)

classifier = GaussianNB()
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(accuracy)
