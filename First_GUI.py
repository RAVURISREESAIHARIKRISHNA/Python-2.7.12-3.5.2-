import Tkinter

obj=Tkinter.Tk()
root.iconbitmap(r'c:\Python27\DLLs\My_Icon.ico')
#Creating a Label..

TheLabel = Tkinter.Label(obj,text='FIRST GUI PROGRAM')

# Packing the label inside the Window...

TheLabel.pack()

# Keeping THe Window Untill The Exit Was Pressed

obj.mainloop()
