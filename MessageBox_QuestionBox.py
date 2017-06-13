from tkinter import*
import sys
import tkinter.messagebox

root = Tk()
root.iconbitmap(r'C:\Users\HARI\AppData\Local\Programs\Python\Python35-32\DLLs\My_Icon.ico')
root.wm_title("Warning and Answer Creation")
"""
Showing Message BOX:

tkinter.messagebox.showinfo("Window Title","Your Message")

This Appears with a OK Button..
"""
tkinter.messagebox.showinfo("Hari Technologies","Thanks For Chosing us!!")
"""
Asking Qustion Box:
    It has YES and NO Buttons
ANswer = tkinter.messagebox.askquestion("Window Title","Question")
And it Returns YES or NO
"""
Answer = tkinter.messagebox.askquestion("Hari Technologies","You owe me 1000$")
if(Answer == 'yes'):
    print("Yes,you owe me 1000$")
    sys.exit(0)
if(Answer == 'no'):
    print("No,You owe me 1000$")
    sys.exit(0)

root.mainloop()
