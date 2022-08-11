from types import NoneType
import requests
import json
import tkinter as tk


def api():
    id = e.get()
    balance = e2.get()
    setbalance = f'https://coderlog.top/api/goit/?key=5b15bdfa142761a1c65f50e046b6f7f5&method=setbalance&user={id}&balance={balance}'
    requests.get(setbalance)
    url = f'https://coderlog.top/api/goit/?key=5b15bdfa142761a1c65f50e046b6f7f5&method=getdata&user={id}'
    res = requests.get(url)
    json = res.json()
    for i in json:
        user_id = i["id"]
        user_name = i["name"]
        user_surname = i["surname"]
        user_email = i["email"]
        user_school_group = i["school_group"]
        user_status = i["status"]
        user_balance = i["balance"]
        if i["id"] is None:
            text_box.insert("1.0", 'Error')
        else:
            text_box.insert("1.0", i)

    

w = tk.Tk()
w.title("My app")
w.minsize(width=100, height=100)
w.maxsize(width=350, height=350)
w.geometry("500x300")


e = tk.Entry()
e.pack()

e2 = tk.Entry()
e2.pack()

text_box = tk.Text()
text_box.pack()

b = tk.Button(text ='Update balance', width=20, height=5, command=api)
b.pack()
w.mainloop()