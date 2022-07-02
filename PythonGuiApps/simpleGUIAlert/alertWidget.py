import tkinter 

import schedule
import time

from tkinter import ttk

def func():
    root =  tkinter.Tk()
    root.geometry("700x350")
    ttk.Label(root, text="Take a walk! OR \n\nSit Straight! OR \n\nDrink Water!",padding=(60,60)).pack()
    root.lift()
    root.focus_force()
    root.mainloop()
        

schedule.every(5).seconds.do(func)

while(True):
    schedule.run_pending()


