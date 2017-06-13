import pyperclip,sys
print("The ClipBoard Data is:")
Data = pyperclip.paste()
print(str(Data))
print("Do you Really Want to Tamper?::Press Enter to Tamper::Press Any Key and Enter to Exit")
h = input()
if(h==""):
    pyperclip.copy("Tampered")
    sys.exit(0)
