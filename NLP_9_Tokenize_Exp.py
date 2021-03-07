#Sent and Word Tokenization without using the NLTK lib or the inbuilt functions/features
#author Eshan K Kaushal
#



file  = open("V8_Engines.txt", "r")
sample = file.read()
#print(sample)
nl = []
nl2=[]
word = ''

for i in sample:
        if i == ' ':
            nl.append(word) #if space then add
            word = ''
        else:
            word += i       #no space but a word, add a word
        #nl.append(word)
if word:                # if a word then add
    nl.append(word)

print("Here:")    
print(nl)


#sentence tokenization
word = ''
for i in sample:
        if i == '.': #finding the sentence boundary i.e is marked by the full stop
                    #if full stop found, do the appending 
            nl2.append(word) #if space then add
            word = ''
        else:
            word += i       #no space but a word, add a word
        #nl.append(word)
if word:                # if a word then add
    nl2.append(word)

print("Here:")    
print(nl2)
