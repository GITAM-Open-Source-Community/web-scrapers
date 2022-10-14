from tkinter import *
import requests
from bs4 import BeautifulSoup
import html5lib
import re
from copy import copy


window = Tk()
window.geometry('300x550')
window.title('Emails from the Link')
entry1 = StringVar()
def fetch():
    try: 
        url = entry1.get()
        r = requests.get(url)
        content = r.text
        soup = BeautifulSoup(content, 'html5lib')
        mail_text = (soup.get_text())
        eml_reg_exp = re.findall(r"[a-zA-Z0-9]+@+[a-zA-Z]+\.[a-zA-Z]+" , mail_text)
        ins = ""
        for value in eml_reg_exp:
            ins += value+'\n'
        ins2 = copy(ins)
        text.config(state= "normal")
        text.insert(INSERT,ins2)

    except Exception:
        print("No Email Found")
    
    return fetch




Label(window,text= "Give me a Link:").grid(row= 0, column =1)

Label(window, text= "URL: ").grid(row=2 , column =0)
Entry(window,textvariable = entry1).grid(row=2, column =1)

btn = Button(window,text= "Get Email", command = fetch)
btn.grid(row =3, column =1,pady = 12)

text =Text(window,width = 29, height = 13)
text.grid(row= 5 , column= 1, pady= 3, padx= 2)


window.mainloop()