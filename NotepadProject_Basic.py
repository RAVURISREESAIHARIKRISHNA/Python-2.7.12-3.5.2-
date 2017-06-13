import os

print("Enter Text in \"\"\" <Text> \"\"\" Format")
Text = input()
print("Enter File name (Do not Enter .txt)")
FileName = input()
FileName += ".txt"
os.chdir("G:\\Python DB")
FileLocation = os.path.join(os.path.abspath("."),FileName)
FileOBJ = open(FileLocation , "w")
FileOBJ.write(Text)
FileOBJ.close()
