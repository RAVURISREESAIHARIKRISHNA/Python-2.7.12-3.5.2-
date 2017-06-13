from Tkinter import*

def PrintName(event):
    print("HEllo World\n")

obj = Tk()

Button_1 = Button(obj,text = " DUDE ",bg="red",fg="white")

#This Just Binds the Button , Event(Pressing Keyboard or a Mouse Button) and The Function...
# Again This Method Should Be PAcked to Get it onthe GUI
Button_1.bind("<Button-1>",PrintName)
# Sheverongs  <>  Are Compulsory
# Button-1  --->  Mouse Left Button
# And this Event should be string  (Event Specification should be in String)


# Packing The Button.....
Button_1.pack()

obj.mainloop()
