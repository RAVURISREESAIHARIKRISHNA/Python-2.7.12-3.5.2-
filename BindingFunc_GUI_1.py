# BUILD ON PYTHON 2.7.12

# For Python 3.0+ Tkinter is tkinter

from Tkinter import*

### BINDING FUNCTIONS WITH GUI

def PrintName():
    print("HELLO WORLD!!\nGot an Instruction from GUI\n")

#GUI Object
obj=Tk()

#  Creating a Button
"""
DO NOT FORGET THE command = FunCtionNAME  ...

command word

Rememeber this......
"""
Button_1 = Button(obj,text="CLICK ME  !",bg="red",fg="white",command=PrintName)
# No Paranthesis For the Function..
#  OBSERVE

# Packing it..

Button_1.pack()

obj.mainloop()
