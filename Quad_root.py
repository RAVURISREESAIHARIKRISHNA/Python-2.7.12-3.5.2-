import math
def Answer(a,b,c):
  if(((b**2)-(4*a*c))>0):
    print("\n1st Root is :\n")
    print(str((-b+math.sqrt((b**2)-(4*a*c))))/(2*a))
    print("\n2nd Root is:\n")
    print(str((-b-math.sqrt((b**2)-(4*a*c))))/(2*a))
    return
  else:
    if(a>0):
      print("\n1st Root is;\n")
      print(str(-b/(2*a))+" + ("+str(math.sqrt(-((b**2)-(4*a*c))))+" i)")
      print("\n2nd Root is:\n")
      print(str(-b/(2*a))+" - ("+str(math.sqrt(-((b**2)-(4*a*c))))+" i)")
      return
    if(a<0):
      print("\n1st Root is:\n")
      print(str(-b/(2*a))+" - ("+str(math.sqrt(-((b**2)-(4*a*c))))+" i)")
      print("\n2nd Root is:\n")
      print(str(-b/(2*a))+" + ("+str(math.sqrt(-((b**2)-(4*a*c))))+" i)")
      return

print("\nEnter X^2 Coefficient:\n")
a=float(input())
while(a==0):
  print("\nRETRY...")
  a=float(input())
print("\nEnter X coefficient:\n")
b=float(input())
print("\nEnter constant:\n")
c=float(input())
Answer(a,b,c)
