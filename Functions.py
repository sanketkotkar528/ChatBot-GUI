# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 12:54:10 2020

@author: Sanket Kotkar 

Title: Functions for generating responce of ChatBot
"""
#%%

# Importing the required libraries 
import pandas as pd
import numpy as np
import nltk
import random
import string
import warnings
warnings.filterwarnings('ignore')
from nltk import sent_tokenize
#%%  downliading the imp modules

nltk.download('punkt',quiet = True )
#%%  
# Function for greeting responce 

def greeting_responce(Text):
    # Lowering the text 
    Text = Text.lower()
    
    # Bot greetings reponce
    bot_greeings = ['Namaskar','Hi','Hey there','Namaskar','Hello']
    
    # User greetings
    user_greetings = ['hi','hey','hello','hola','greetings','wassup','namaskar']
    
    for word in Text.split():
        if word in user_greetings:
            return random.choice(bot_greeings)

#%%  
# Function for index sort

def index_sort(list_var):
    
    length = len(list_var)
    
    list_index = list(range(0,length))
    
    x = list_var
    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > x[list_index[j]]:
                #Swap
                Temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = Temp
    
    return list_index
    
#%%
# Function for Bot responce

#Create bot response
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def bot_response(user_input, Corpus):
    user_input=user_input.lower()
    Sent_List = Corpus
    Sent_List.append(user_input)
    bot_response=''
    cm=TfidfVectorizer().fit_transform(Sent_List)
    similarity_scores=cosine_similarity(cm[-1],cm)
    similarity_scores_list=similarity_scores.flatten()
    index=index_sort(similarity_scores_list)
    index=index[1:]
    
    response_flag=0
    
    
    j = 0
    for i in range(len(index)):
        if similarity_scores_list[index[i]]>0.0:
            bot_response=bot_response+''+ Sent_List[index[i+1]] + ' ' + Sent_List[index[i+2]] + ' ' + Sent_List[index[i+3]]
            response_flag=1
            j=j+1
        if j > 2:
            break
            
        if response_flag==0:
             bot_response=bot_response+''+"I apologize I dont understand"
                  
        Sent_List.remove(user_input)
        return bot_response

#%%  
# Function for Tokenize 

def Tokenize_Sentence(Corpus):
    return sent_tokenize(Corpus)
#%%  

