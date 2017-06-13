def Divide(a,b):
  try:
    return (a/b)
  except ZeroDivisionError:
    print("\nHey!Dont be insane!\n")


def Rem(a,b):
  try:
    return (a%b)
  except ZeroDivisionError:
    print("\nHey!Dont be insane!\n")

print("Enter Operand1:\n")
oper1=float(input())
print("Enter Operand2:\n")
oper2=float(input())
while(True):
  print("\n")
  print("********MENU*********\n")
  print("1.Addition\n")
  print("2.Operand1-Operand2\n")
  print("3.Operand2-Operand1\n")
  print("4.Operand1 Multi Operand2\n")
  print("5.Operand1 / Operand2\n")
  print("6.opernad1 % Operand2\n")
  print("7.Operand2 / Operand1\n")
  print("8.Operand2 % Operand1\n")
  print("9.Operand1 ^ Operand2\n")
  print("10.Operand2 ^ Operand1\n")
  print("11.EXIT\n")
  print("\n\nEnter your Option:\n")
  ch=int(float(input()))
  if(ch>11 and ch<1):
    print("\nWrong Entery!!!\nRetry...")
    continue
  if(ch==1):
    print(oper1+oper2)
    continue
  if(ch==2):
    print(oper1-oper2)
    continue
  if(ch==3):
    print(oper2-oper1)
    continue
  if(ch==4):
    print(oper1*oper2)
    continue
  if(ch==5):
    x=Divide(oper1,oper2)
    if(x!=None):
      print(x)
    continue
  if(ch==6):
    x=Rem(oper1,oper2)
    if(x!=None):
      print(x)
    continue
  if(ch==7):
    x=Divide(oper2,oper1)
    if(x!=None):
      print(x)
    continue
  if(ch==8):
    x=Rem(oper2,oper1)
    if(x!=None):
      print(x)
    continue
  if(ch==9):
    print(oper1**oper2)
    continue
  if(ch==10):
    print(oper2**oper1)
    continue
  
  if(ch==11):
    print("\n****BYE***")
    exit()
 
