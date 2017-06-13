import pyperclip,webbrowser,sys
CheckUrl = pyperclip.paste()
print("Works only With FAMOUS URLs\nPerfect Version will beavailable Soon")
print("Press Enter to Continue/Else any other key to Exit")
h = input()
if h!="":
	sys.exit(0)
if("www." in CheckUrl):
    webbrowser.open(CheckUrl)
else:
    webbrowser.open("file:///G:/HTML%20Sources/For_Python.html")
