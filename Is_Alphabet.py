import sys
print("\nEnter a cahracter:\n")
ch=input()
while(len(ch)!=1):
  print("\nRETRY..")
  ch=input()
if((ord(ch)>=ord('a') and ord(ch)<=ord('z'))or(ord(ch)>=ord('A') and ord(ch)<=ord('Z'))): #using ord() to Compare ASCII Values
  print("\n{} is a character".format(ch))
  sys.exit()
print("\n{} is not a character".format(ch))
