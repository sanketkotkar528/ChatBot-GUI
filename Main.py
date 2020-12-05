# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 12:56:16 2020

@author: Sanket Kotkar

Title: 
"""
#%%  importing the functions file for using the fuctions to built the ChatBot  
import Functions
#%% Loading the data 

with open("D:/CMS/CMS_2019/Chatbot/diabetes_data_1.txt",'r',encoding = 'utf8') as f:
    Data = f.read()

Data = Functions.Tokenize_Sentence(Data)
Corpus = Data

#%%  Importing the tkinter library for defining the desktop application
from tkinter import *
#%%  developing the bot backgroung 

# Imporing the library and modules 
import pandas as pd
import numpy as np
import nltk
import random
import string
import warnings
warnings.filterwarnings('ignore')

# Function to operate the chatbot
def Chat(query,Corpus):
    user_input = query
    exit_list=['exit','bye','see you later','quit','break','no','thanks','thanks alot']
    if user_input.lower() in exit_list:
        print( "Ok, Thanks, Bye...")
        return( "Ok, Thanks, Bye...,\
               Stay Home, Stay Safe!!!")
    elif user_input.lower() in ['ok','hmm','its ok']:
        return ' Can I tell you more about it'
    elif user_input.lower() in ['yes','ok']:
        return  Functions.bot_response(user_input, Corpus)
    else:
        if Functions.greeting_responce(user_input) != None:
            return  Functions.greeting_responce(user_input)
        else:
            return  Functions.bot_response(user_input, Corpus)



#%%  

main = Tk()

main.geometry("600x600")    # Defining the geometry of box for chatbot 
main.title(" Doc Bot ")     # Defining the title of chatbot Hi

img = PhotoImage(file="Bot_3.png")  # Loading the image file
photoL = Label(main, image=img )    # Creating thePhotoL class to fit the image 
photoL.pack(pady =5 )

def ask_from_bot():
    query = textF.get()
    query_1 = str(query)
    answer_from_bot = Chat(query_1, Corpus=Corpus)
    msgs.insert(END,"You :"+ query)
    print(type(answer_from_bot))
    msgs.insert(END,"Doc Bot :"+ str(answer_from_bot))
    textF.delete(0,END)
    msgs.yview(END)
    
    


frame = Frame(main)               # Defining the class for frame

sc = Scrollbar(frame)             # Defining the class for scrollbar

msgs = Listbox(frame, width = 80 , height = 20, yscrollcommand = sc.set)

sc.pack(side = RIGHT, fill= Y)
msgs.pack(side = LEFT, fill = BOTH)
frame.pack(pady = 10)

# Creating the text filles box ( Input box )
textF = Entry(main, font=("verdana",20))
textF.pack(fill=X, pady = 10 )

# Creating the buttun for click 
btn = Button(main, text="Ask me !!", font=("verdana",20), command= ask_from_bot )
btn.pack()

# Define function for enter 
def enter(event):
    btn.invoke()

# Binding main window with bind key
main.bind('<Return>',enter)


main.mainloop()
#%%