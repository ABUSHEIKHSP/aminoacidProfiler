from lib2to3.pgen2 import driver
import tkinter as tk
from tkinter import *
from script import Coronavar
import webbrowser
import os


result = tk.Tk()
result.title('Result')
result.geometry('600x400+50+50')

def Excel():
    os.system('libreoffice result.csv')

gap = tk.Label(result)
gap.pack()

msg = tk.Label(result, text=f'The "result.csv" file is stored in the\nmain folder you selected')
msg.pack()

gap = tk.Label(result)
gap.pack()

excel = Button(text='view in excel',command=Excel)
excel.pack()

def goto_link():
    webbrowser.open('https://signature-uc636sdsia-as.a.run.app/')


gap = tk.Label(result)
gap.pack()

signature_identifier = Button(text='Amino acid Signature', command=goto_link)
signature_identifier.pack()





