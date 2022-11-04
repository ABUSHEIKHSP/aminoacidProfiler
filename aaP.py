

from tkinter import *
import tkinter as tk
from tkinter import filedialog as fd
import os
from refracted import aminoacidProfiler




root = tk.Tk()


root.title('aminoacidProfiler')

root.geometry('600x400+50+50')

message = tk.Label(root,text='This is a program for amino acid profiling' )
message.pack()

gap = tk.Label(root)
gap.pack()



def get_path():
    global folder
    folder = fd.askdirectory()
    aminoacidProfiler.run_control(folder)
    os.chdir(folder)
    root.destroy()
    import page2

    
enter_btn = tk.Button(text='select folder',command=get_path)
enter_btn.pack()





root.mainloop()
    
