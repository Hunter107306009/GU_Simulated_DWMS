#!/usr/bin/python
# -*- coding: UTF-8 -*
import default
import transaction
import tkinter as tk
from tkinter import Button
from tkinter import PhotoImage
from tkinter import Label
from tkinter import Entry

def combineT(): 
    transaction.main()
    showN()

def showN():
	lable1.config(text="進行了"+str(transaction.T_time)+"次交易")
	lable1.pack()
	lable2.config(text="獲得了"+str(transaction.New_time)+"個新用戶")
	lable2.pack()
	lable3.config(text="終止時間:"+str(transaction.date))
	lable3.pack()


M_Frame= tk.Tk()
M_Frame.title("DB Control")
M_Frame.geometry("900x400")
M_Frame.resizable(False,False)
M_Frame.config(background="#CAFFFF")
M_Frame.attributes("-topmost",1)

btn1=Button(text="模擬交易",command=combineT)
btn1.config(width=10,height=2)
btn1.place(anchor=tk.CENTER,x=400,y=200)
btn2=Button(text="回復預設值",command=default.main)
btn2.config(width=10,height=2)
btn2.place(anchor=tk.CENTER,x=500,y=200)

lable1=Label(text="進行了N次交易",background="#CAFFFF",fg="black")
lable1.pack()
lable2=Label(text="獲得了N個新用戶",background="#CAFFFF",fg="black")
lable2.pack()
lable3=Label(text="起始時間:2021-01-01",background="#CAFFFF",fg="black")
lable3.pack()

M_Frame.mainloop()