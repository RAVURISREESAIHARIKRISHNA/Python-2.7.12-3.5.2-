#Build for Python 2.7.12
from Tkinter import*

def Left(event):
    print("Left Button")
def Right(event):
    print("Right Button")
def Middle(event):
    print("Middle Button")


obj = Tk()
root.iconbitmap(r'c:\Python27\DLLs\My_Icon.ico')
Frame_1 = Frame(obj , width=300 , height = 500)
Frame_1.bind("<Button-1>",Left)
Frame_1.bind("<Button-2>",Middle)
Frame_1.bind("<Button-3>",Right)

Frame_1.pack()

obj.mainloop()
