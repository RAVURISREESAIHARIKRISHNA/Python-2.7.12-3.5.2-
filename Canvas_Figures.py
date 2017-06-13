from tkinter import*

root = Tk()
root.iconbitmap(r'C:\Users\HARI\AppData\Local\Programs\Python\Python35-32\DLLs\My_Icon.ico')
root.wm_title("Canvas")
"""
Creating a Canvas
->CanvasOBJ = Canvas(root , width = <Width> ,height = <Height>)

->After Creating we should pack it.
"""
WhiteBoard = Canvas(root,width = 500, height = 500)
WhiteBoard.pack()

#Drawing a Line
"""
	LineName = CanvasOBJ.create_line(x1,y1,x2,y2,fill = "red")
	As it is associated to the Canvas no need to pack it..(CanvasOBJ is already packed)
"""
RedLine = WhiteBoard.create_line(0,0,200,200,fill = "red")
#Drawing another Line
greenLine = WhiteBoard.create_line(100,200,10,0,fill = "black")
Box = WhiteBoard.create_rectangle(500,500,400,400,fill = "yellow")
Circle = WhiteBoard.create_circle(250,250,100,fill = "red")

root.mainloop()
