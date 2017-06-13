#Build for Python 2.7.12
from tkinter import*

def Left(event):
    print("Left Button")
def Right(event):
    print("Right Button")
def Middle(event):
    print("Middle Button")


obj = Tk()
obj.iconbitmap(r'C:\Users\HARI\AppData\Local\Programs\Python\Python35-32\DLLs\My_Icon.ico')
Frame_1 = Frame(obj , width=300 , height = 500)
Frame_1.bind("<Button-1>",Left)
Frame_1.bind("<Button-2>",Middle)
Frame_1.bind("<Button-3>",Right)

Frame_1.pack()

obj.mainloop()
