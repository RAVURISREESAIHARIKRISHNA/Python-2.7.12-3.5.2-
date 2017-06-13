#Build on Python 2.7.12

from tkinter import*
import sys

def New():
    print("\nPressed New\n")
def Print():
    print("\nPressed Print\n")
def Open():
    print("\nPressed Open\n")
def Save():
    print("\nPressed Save\n")
def SaveAs():
    print("\nPresses Save As\n");
def PageSetup():
    print("\nPressed Page Setup\n")
def Undo():
    print("\nPressed UNDO\n")
def Cut():
    print("\nPressed Cut\n")
def Copy():
    print("\nPressed Copy\n")
def Paste():
    print("\nPressed Paste\n")
def Delete():
    print("\nPressed Delte\n")
def Find():
    print("\nPressed Find\n")
def FindNext():
    print("\nPressed Find Next\n")
def Replace():
    print("\nPressed Replace\n")
def GoTo():
    print("\nPressed GoTo\n")
def SelectAll():
    print("\nPressed Select All\n")
def TimeDate():
    print("\nPressed Time/Date\n")
def WordWrap():
    print("\nPressed Word Wrap\n")
def Font():
    print("\nPressed Font\n")
def ViewHelp():
    print("\nPressed View Help\n")
def StatusBar():
    print("\nPressed Status Bar\n")
def About():
    print("\nPressed About\n")

root = Tk()
root.wm_title("Notepad Mimic")
root.iconbitmap(r'c:\Python27\DLLs\My_Icon.ico')

MainMenu = Menu(root)
root.config(menu = MainMenu)

FileMenu = Menu(MainMenu)
MainMenu.add_cascade(label = "File",menu = FileMenu)
FileMenu.add_command(label = "New",command = New)
FileMenu.add_command(label = "Open...",command = Open)
FileMenu.add_command(label = "Save",command = Save)
FileMenu.add_command(label = "Save As",command = SaveAs)
FileMenu.add_separator()
FileMenu.add_command(label = "Page Setup...",command = PageSetup)
FileMenu.add_command(label = "Print...",command = Print)
FileMenu.add_separator()
FileMenu.add_command(label = "Exit",command = sys.exit)

EditMenu = Menu(MainMenu)
MainMenu.add_cascade(label = "Edit",menu = EditMenu)
EditMenu.add_command(label = "Undo",command = Undo)
EditMenu.add_separator()
EditMenu.add_command(label = "Cut",command = Cut)
EditMenu.add_command(label = "Copy",command = Copy)
EditMenu.add_command(label = "Paste",command= Paste)
EditMenu.add_command(label="Delete",command = Delete)
EditMenu.add_separator()
EditMenu.add_command(label = "Find...",command = Find)
EditMenu.add_command(label = "Find Next",command=FindNext)
EditMenu.add_command(label = "Replace...",command = Replace)
EditMenu.add_command(label="Go To...",command=GoTo)
EditMenu.add_separator()
EditMenu.add_command(label="Select All",command=SelectAll)
EditMenu.add_command(label ="Time/Date",command=TimeDate)

FormatMenu = Menu(MainMenu)
MainMenu.add_cascade(label = "Format",menu = FormatMenu)
FormatMenu.add_command(label = "Word Wrap",command = WordWrap)
FormatMenu.add_command(label = "Font...",command = Font)

ViewMenu = Menu(MainMenu)
MainMenu.add_cascade(label = "View",menu = ViewMenu)
ViewMenu.add_command(label="Status Bar",command = StatusBar)

HelpMenu = Menu(MainMenu)
MainMenu.add_cascade(label = "Help",menu = HelpMenu)
HelpMenu.add_command(label = "View Help",command = ViewHelp)
HelpMenu.add_separator()
HelpMenu.add_command(label = "About Notepad",command = About)


root.mainloop()
