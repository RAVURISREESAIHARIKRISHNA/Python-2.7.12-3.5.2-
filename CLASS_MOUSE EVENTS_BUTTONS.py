from Tkinter import*

class MouseEvents:

    #IT SHOULD TAKE TWO ARGUMENTS event AND self
    def Left(self,event):
        print("LEFT")
    def Middle(self,event):
        print("MIDDLE")
    def Right(self,event):
        print("RIGHT")


    def __init__(self,master):

        frame = Frame(master)
        frame.pack()

        self.MainButton = Button(frame , text="MOUSE EVENTS" , bg = "red" , fg = "white")
        self.MainButton.bind("<Button-1>",self.Left)
        self.MainButton.bind("<Button-2>",self.Middle)
        self.MainButton.bind("<Button-3>",self.Right)
        self.MainButton.pack()

        self.QuitButton = Button(frame, text="QUIT" , bg="black" ,fg = "white" , command = frame.quit)
        self.QuitButton.pack()
  

root=Tk()
root.iconbitmap(r'c:\Python27\DLLs\My_Icon.ico')
obj=MouseEvents(root)

root.mainloop()
