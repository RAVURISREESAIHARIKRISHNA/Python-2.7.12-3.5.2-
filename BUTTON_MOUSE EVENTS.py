from Tkinter import*

def Left(event):
    print("Left Button")
def Right(event):
    print("Right Button")
def Middle(event):
    print("Middle Button")

obj = Tk()

Button_1 = Button(obj , text="MOUSE EVENTS" , bg= "red" , fg = "white")

Button_1.bind("<Button-1>",Left)
Button_1.bind("<Button-2>",Middle)
Button_1.bind("<Button-3>",Right)

Button_1.pack()

obj.mainloop()
