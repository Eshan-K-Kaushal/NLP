#author ESHAN K KAUSHAL - 17103116
#The Code Below (1)finds the number of lines, (2)number of words and (3)the tag words
#and (4)does sentence and word tokenization and (5)stop word removal and (6)stemming.
#Just change the text doc in the file = open() line
import nltk
import threading
import logging
from nltk.corpus import state_union
from nltk.corpus import stopwords
from nltk import tokenize
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tokenize import sent_tokenize, word_tokenize
from langdetect import detect
from nltk.stem import PorterStemmer
ps = PorterStemmer()

exit_exit = ["Bye", "bye", "Goodbye", "goodbye", "talk to you later",
                 "bye-bye", "bye bye", "byebye", "ByeBye",
                     "TTYL", "BB", "B", "GG", "b", "gg", "exit", "Exit", "EXIT", "N", "NO", "n", "no"]

stop_words = set(stopwords.words("english"))
#nltk.download('state_union')
#nltk.download('averaged_perceptron_tagger')

#print(sample_txt.readable())    
#print(sample_txt.read())
#no of lines
file = open("V8_Engines.txt", "r")
counter = 0
sample_txt = file.read()
lines  = sample_txt.split("\n")
for i in lines:
    if i:
        counter += 1
print("The number of lines in the document is:")
print(counter)

words = sample_txt.split()
print("The number of words in the document is:")
print(len(words))

print("The language of the document is:")
print(detect(sample_txt))
print("\n")

print("Every word tagged:")
train_text = state_union.raw("2005-GWBush.txt") # to train


custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_txt)

def tag_words():
    for i in tokenized:
        words = nltk.word_tokenize(i)
        tagged = nltk.pos_tag(words)
        print(tagged)
        print('\n')

    

tag_words()
while(True):
    print("Do you want futher features as tokenization, stop word removal and stemming?")
    print("Type Yes if you want and 'no' or 'exit' if you want to leave")
    choice = input()
    if((choice == 'YES') | (choice == 'Yes') | (choice == 'yes') | (choice == 'y') | (choice == 'Y')):
        print("What feature do you want?")
        print("Type 1 for Word Tokenization")
        print("Type 2 for Sentence Tokenization")
        print("Type 3 for Stop Word removal")
        print("Type 4 for Stemming")
        choice_1 = input()
        if(choice_1 == '1'):
            print("Word Tokenized:")
            s_t_w = word_tokenize(sample_txt)
            for i in s_t_w:
                print(i)
        elif(choice_1 == '2'):
            print("Sentence Tokenize")
            s_t_s = sent_tokenize(sample_txt)
            for i in s_t_s:
                print(i)
        elif(choice_1 == '3'):
            s_words = word_tokenize(sample_txt)
            st_wds_remd = []
            for i in s_words:
                if i not in stop_words:
                    st_wds_remd.append(i)
            print(st_wds_remd)
        elif(choice_1 == '4'):
            s_words = word_tokenize(sample_txt)
            for i in s_words:
             print("Caution: It may not be proper.")   
             print(ps.stem(i))
        else:
            print("Thanks")

    elif any(x in choice for x in exit_exit):
        print("Thanks for showing your interest")
        break
    
    






