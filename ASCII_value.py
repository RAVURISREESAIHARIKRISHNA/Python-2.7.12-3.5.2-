print("Enter a character:\n")
ch=input()
while(len(ch)!=1):
  print("\nShould Enter single Character...RETRY!")
  ch=input()
print(ord(ch))
