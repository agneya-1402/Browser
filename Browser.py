import webbrowser
import tkinter as tk
from tkinter import *


a=tk.Tk()
a.title("Browser")
a.iconbitmap("C:/Users/dhiraj/Pictures/Browser_img/Google_logo.png")


def search():
    word=SearchBar.get()
    webbrowser.open(word)

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
google.grid(row=1,column=0)

iyoutube=PhotoImage(file="C:/Users/dhiraj/Pictures/Browser_img/Youtube_logo.png")
youtube=tk.Button(a,text="Youtube",image=iyoutube,command=youtube)
youtube.grid(row=1,column=1)

itwitter=PhotoImage(file="C:/Users/dhiraj/Pictures/Browser_img/Twitter_logo.png")
twitter=tk.Button(a,text="Twitter",image=itwitter,command=twitter)
twitter.grid(row=1,column=2)

ifacebook=PhotoImage(file="C:/Users/dhiraj/Pictures/Browser_img/Facebook_logo.png")
facebook=tk.Button(a,text="facebook",image=ifacebook,command=facebook)
facebook.grid(row=1,column=3)

iamazon=PhotoImage(file="C:/Users/dhiraj/Pictures/Browser_img/Amazon_logo.png")
amazon=tk.Button(a,text="amazon",image=iamazon,command=amazon)
amazon.grid(row=1,column=4)

SearchButton=tk.Button(a,text="Search",command=search,bg="blue",fg="white")
SearchButton.grid(row=0,column=3)

a.mainloop()


