import webbrowser
import tkinter as tk
from tkinter import *
import speech_recognition as sr

r=sr.Recognizer()

a=tk.Tk()
a.title("Browser")
a.iconbitmap("C:/Users/dhiraj/Pictures/Browser_img/Google_logo.png")


def search():
    word=SearchBar.get()
    webbrowser.open(word)

def voice():
    with sr.Microphone() as source:
        #print("Say Something :")
        L1=Label(a,text="Listening...")
        L1.grid(row=1,column=2)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            webbrowser.open(text)
            L2=Label(a,text=f"Searching {text}...")
            L2.grid(row=1,column=2)
            #print(f"You said :{text}\n")
        except:
            print("error")
            L3=Label(a,text="Try Again...!!!")
            L3.grid(row=3,column=2)


def google():
    webbrowser.open("https://google.com")

def youtube():
    webbrowser.open("https://www.youtube.com/?gl=IN")

def twitter():
    webbrowser.open("https://twitter.com")

def facebook():
    webbrowser.open("https://www.facebook.com/")

def amazon():
    webbrowser.open("https://www.amazon.in/")



SearchBar=tk.Entry(a,bd=15)
SearchBar.grid(row=0,column=2)

igoogle=PhotoImage(file="C:/Users/dhiraj/Pictures/Browser_img/Google_logo.png")
google=tk.Button(a,text="Google",image=igoogle,command=google)
google.grid(row=0,column=0)

#iyoutube=PhotoImage(file="C:/Users/dhiraj/Pictures/Browser_img/Youtube_logo.png")
#youtube=tk.Button(a,text="Youtube",image=iyoutube,command=youtube)
#youtube.grid(row=1,column=1)

#itwitter=PhotoImage(file="C:/Users/dhiraj/Pictures/Browser_img/Twitter_logo.png")
#twitter=tk.Button(a,text="Twitter",image=itwitter,command=twitter)
#twitter.grid(row=1,column=2)

#ifacebook=PhotoImage(file="C:/Users/dhiraj/Pictures/Browser_img/Facebook_logo.png")
#facebook=tk.Button(a,text="facebook",image=ifacebook,command=facebook)
#facebook.grid(row=1,column=3)

#iamazon=PhotoImage(file="C:/Users/dhiraj/Pictures/Browser_img/Amazon_logo.png")
#amazon=tk.Button(a,text="amazon",image=iamazon,command=amazon)
#amazon.grid(row=1,column=4)

isearch=PhotoImage(file="C:/Users/dhiraj/Pictures/Browser_img/search.png")
SearchButton=tk.Button(a,image=isearch,command=search)
SearchButton.grid(row=0,column=3)

ivoice=PhotoImage(file="C:/Users/dhiraj/Pictures/Browser_img/Mic.png")
Mic=tk.Button(a,image=ivoice,command=voice)
Mic.grid(row=0,column=4)
#Add voice search....!!!!

a.mainloop()


