import tkinter as tk
from tkinter import Entry, Label, Button
import webbrowser



root = tk.Tk()
root.title("ai assistance")

root.configure(bg='yellow')


def youtube_search():
    query = entry.get()
    url = f'https://www.youtube.com/results?search_query={query}'
    webbrowser.open(url)


def google_search():
    query = entry.get()
    url = f'https://google.com/search?q={query}'
    webbrowser.open(url)


def insta_search():
    query = entry.get()
    Username = entry.get().replace("@", '')
    url = f'www.instagram.com/{Username}/'
    webbrowser.open(url)

def twitter_search():
    query=entry.get()
    Username=entry.get().replace("@","")
    url = f"www.twitter.com/{Username}/"
    webbrowser.open(url)



Label(root, text='enter your command:').pack(pady=10)
entry = Entry(root, width=50)
entry.pack(pady=10)

Button(root, text='search on youtube', command=youtube_search).pack(pady=5)
Button(root, text='search on google', command=google_search).pack(pady=5)
Button(root, text='search on instagram', command=insta_search).pack(pady=5)
Button(root,text="search on twitter",command=twitter_search).pack(pady=5)

root.mainloop()
