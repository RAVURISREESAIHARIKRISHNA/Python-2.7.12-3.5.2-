from Tkinter import*

obj=Tk()
root.iconbitmap(r'c:\Python27\DLLs\My_Icon.ico')

#Creating  invisible Frames...

# Fisrt Frame will be top by Default...

TopFrame = Frame(obj)
TopFrame.pack()

#For Down FRAME we have to specify BOTTOM while packing it in.

BottomFrame = Frame(obj)
BottomFrame.pack(side=BOTTOM)

#CREATING BUTTONS...

"""
Button(FrameName (or) GUIobject,text="Your Text",bg="BackgroundColorName",fg="ForegroundColorName")
"""
Button1 = Button(TopFrame,text="BUTTON 1",bg="yellow",fg="red")
Button2 = Button(TopFrame,text="BUTTON 2",bg="green",fg="blue")
Button3 = Button(TopFrame,text="BUTTON 3",bg="black",fg="green")

Button4 = Button(BottomFrame,text="BUTTON 4",bg="white",fg="black")

#PACKING BUTTONS....

Button1.pack(side=LEFT)
Button2.pack(side=LEFT)
Button3.pack(side=LEFT)

Button4.pack(side=RIGHT)

obj.mainloop()
