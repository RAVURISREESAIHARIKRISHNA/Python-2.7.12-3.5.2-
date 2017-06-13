from tkinter import*

obj=Tk()
obj.iconbitmap(r'C:\Users\HARI\AppData\Local\Programs\Python\Python35-32\DLLs\My_Icon.ico')

Name_Label = Label(obj,text="Login ID")
Password_Label = Label(obj,text="Password")

Name_Entry = Entry(obj)
Password_Entry = Entry(obj,show='*')

Name_Label.grid(row=0,column=0,sticky=E)
Password_Label.grid(row=1,column=0,sticky=E)

Name_Entry.grid(row=0,column=1)
Password_Entry.grid(row=1,column=1)

#Check Box
Check_Box = Checkbutton(obj,text="Keep Me Logged in")

Check_Box.grid(row=2,column=0,columnspan=2)


SignIn_button = Button(obj,text="SIGN IN",bg="red",fg="white")
SignIn_button.grid(row=3,column=0,rowspan=4,columnspan=4)

obj.mainloop()
