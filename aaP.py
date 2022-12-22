#!pyenv/bin/python3

import os

os.system('/bin/bash --rcfile act.sh')

import tkinter as tk
from tkinter import filedialog as fd, ttk
import webbrowser
from refracted import aminoacidProfiler

class aaP:

    def goto_link(self):
        webbrowser.open('https://signature-uc636sdsia-as.a.run.app/')

    def Excel(self):
  
        os.system('libreoffice result.csv')
        

    def page2(self):

        self.page2_frame = ttk.Frame(self.notebook)
        self.page2_frame.pack(fill='both', expand=True, padx=5)
        self.notebook.add(self.page2_frame, text='page2')
        self.notebook.select(self.page2_frame)

        r_label = tk.Label(self.page2_frame, text=f'The "result.csv" file is stored in the\nmain folder you selected')
        r_label.pack(padx=10, pady=10)

        excel = ttk.Button(self.page2_frame, text='view in Excel',command=self.Excel)
        excel.pack(padx=10, pady=10)

        asignor = ttk.Button(self.page2_frame, text='Go to ASiGnor', command=self.goto_link)
        asignor.pack(padx=10, pady=10)

    def get_path(self):

        try:
            self.page2_frame.destroy()
        except:
            pass

        folder = fd.askdirectory()

        if len(folder) > 0:
            aminoacidProfiler.run_control(folder)
            os.chdir(folder)
            self.page2()
        else:
            pass

    def __init__(self):  

        self.root = tk.Tk()
        self.root.title('aminoacidProfiler')
        self.root.geometry('600x400')

        self.root_frame = ttk.Frame(self.root)
        self.root_frame.pack(side='top', fill='both')

        self.w_label = ttk.Label(self.root_frame,text='This is a program for amino acid profiling' )
        self.w_label.pack(padx=10, pady=5)

        self.W_quit = ttk.Button(self.root_frame, text='Quit', command=self.root.destroy)
        self.W_quit.pack(side='right', padx=15)

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)

        self.page1_frame = ttk.Frame(self.notebook)
        self.page1_frame.pack(fill='both', expand=True, padx=5)
        self.notebook.add(self.page1_frame, text='aaP')

        enter_btn = ttk.Button(self.page1_frame, text='select folder',command=self.get_path)
        enter_btn.pack(padx=10, pady=15)

        self.root.mainloop()


aaP()      
    





    
    
