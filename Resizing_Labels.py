from Tkinter import*

obj=Tk()

Label1 = Label(obj,text="LABEL 1",bg="black",fg="white")
Label2 = Label(obj,text="LABEL 2",bg="yellow",fg="blue")
Label3 = Label(obj,text="LABEL 3",bg="green",fg="red")
Label4 = Label(obj,text="LABEL 4",bg="red",fg="black")

BottomFrame = Frame(obj)
BottomFrame.pack(side=BOTTOM)

Button1 = Button(BottomFrame,text="IT IS A BUTTON !!!",bg="white",fg="red")
Button1.pack()

Label1.pack()
Label2.pack(fill=X)
Label3.pack(side=LEFT,fill=Y)
Label4.pack(side=RIGHT,fill=Y)

obj.mainloop()
