#from tkinter import *
try:                        # In order to be able to import tkinter for
    import tkinter as tk    # either in python 2 or in python 3
except ImportError:
    import Tkinter as tk
import glob

# All Directory Link
ENGlISH = """D:\DMS\LMS-Project\SCRIPT_BACKUP\*.sql"""
HINDI   = """D:\DMS\LMS-Project\LMS-REPORT\*.sql"""
SOUTH   = """D:\DMS\LMS-Project\LMS-REPORT\Report Query\*.sql"""

def donothing():
    filewin = tk.Toplevel(root)
    button = tk.Button(filewin, text="Do nothing button")
    button.pack()

#For English Movie
def fetchEnglishMovie():
    #clearScreen()
    for f in glob.iglob(ENGlISH):
        print(f)
        sample = tk.Label(text=f,justify=tk.LEFT)
        sample.pack()

#For Hindi Movie
def fetchHindiMovie():
    for f in glob.iglob(HINDI):
        print(f)
        sample = tk.Label(text=f, justify=tk.LEFT)
        sample.pack()

#For South Movie
def fetchSouthMovie():
    for f in glob.iglob(SOUTH):
        print(f)
        sample = tk.Label(text=f, justify=tk.LEFT)
        sample.pack()

#For Clearing Screen
root = tk.Tk()

menubar = tk.Menu(root)
root.geometry("500x500")

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New",           command=donothing)
filemenu.add_command(label="Open",          command=donothing)
filemenu.add_command(label="Save",          command=donothing)
filemenu.add_command(label="Save as...",    command=donothing)
filemenu.add_command(label="Close",         command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit",          command=root.quit)
menubar.add_cascade(label="File",           menu=filemenu)

moviemenu = tk.Menu(menubar, tearoff=0)
moviemenu.add_command(label="English", command=fetchEnglishMovie)
moviemenu.add_command(label="Hindi",   command=fetchHindiMovie)
moviemenu.add_command(label="South",   command=fetchSouthMovie)


moviemenu.add_separator()

moviemenu.add_command(label="Exit",     command=root.quit)
menubar.add_cascade(label="All Movie",  menu=moviemenu)

root.config(menu=menubar)
root.mainloop()