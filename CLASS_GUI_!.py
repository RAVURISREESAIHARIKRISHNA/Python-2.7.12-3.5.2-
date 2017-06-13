from Tkinter import*



class FrameButton:

    # When Object gets Created It automatically Creates The below defined Environment

    #master is the keyword which receives the GUI object,
    #As we need an GUI object to create the Environment

    
    def __init__(self,master):

        frame = Frame(master)
        frame.pack()

        self.PrintButton = Button(frame , text="Print Message" , bg="red" , fg = "white" , command = self.PrintMessage)
        #PrintMEssage is a Member of This Class and should be called by self Pointer
        self.PrintButton.pack(side=LEFT)

        self.QuitButton = Button(frame , text ="QUIT" , bg="black" , fg="white" ,command = frame.quit)
        #Frame Class has a Function quit(),which is nothing but breaking from the mainloop()
        #Here frame is an instance of Frame


    def PrintMessage(self):
        print(" GOT A COMMAND FROM USER GUI")

    


root = Tk()
root.iconbitmap(r'c:\Python27\DLLs\My_Icon.ico')
obj = FrameButton(root)

root.mainloop()
