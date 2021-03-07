#without the nltk library
#17103116
#still developing the dictionary for the tag words
from langdetect import detect
import re
import matplotlib.pyplot as py
#from nltk import sent_tokenize
midwords = ["a", "is", "an", "are", "the", "they", "these", "was",
            "were", "The", "A", "Were", "Was", "These", "They",
            "Are", "Is", "Their", "their", "From", "from", "has", "Had",
            "Has", "had", "Of", "of", "this", "This"]
file  = open("V8_Engines.txt","r")
counter = 0
c1 = 0
c2 = 0
sample = file.read()
lines = sample.split("\n")
for i in lines:
    if i:
        counter += 1
print("No of lines are:")
print(counter)
words = sample.split()
print("No of words:")
print(len(words))
print("The language of the document is:")
print(detect(sample))

print("\n")
print("Words are:")
for i in sample.split():#word tokenize
    print(i)
print("\n")
print("Sentences are:")
for i in sample.split("\n"): #Tokenize as per new line characters
    print(i)
    print("\n")
print("\n")
print("Filtered Sentence: without any connecting words (stop words).")
fs = []
for i in sample.split():
    if i not in midwords:
        fs.append(i)
        
print(fs)


#for i, each in enumerate (ss, start = 1):
#    print("{}.\t{}".format(i,each))


c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
print("counts of every word:")
for i in sample.split():
    if i == "the" or i == "The":
        c1 +=1
print("Total occurences of 'the' are:")
print(c1)

for i in sample.split():
    if i == 'for' or i == "For":
        c2 +=1
print("Total occurences of 'for' are:")
print(c2)

for i in sample.split():
    if i == 'from' or i == "From":
        c3 +=1
print("Total occurences of 'from' are:")
print(c3)
for i in sample.split():
    if i == 'a' or i == 'A':
        c4 +=1
print("Total occurences of 'a' are:")
print(c4)

for i in sample.split():
    if i == 'were' or i == 'Were':
        c5 +=1
print("Total occurences of 'were' are:")
print(c5)

for i in sample.split():
    if i == 'was' or i == 'Was':
        c6 +=1
print("Total occurences of 'was' are:")
print(c6)

data  = {'a':c4, 'the':'c1'}
names = list(data.keys())
values = list(data.values())

fig, axs = py.subplots(1,3, figsize = (9,3), sharey=True)
