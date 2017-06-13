import sys
"""ArmstringNumber:
abc{3-digit} is an ArmstrongNumber if
abc=(a*a*a)+(b*b*b*)+(c*c*c)
i.e.  abc{3-digit}=(a**3)+(b**3)+(c**3)"""
print("Enter a Number:")
st=input()
n=int(st)
x=n
Len=len(st)
r=0
while(n!=0):
  r=r+((n%10)**Len)
  n=int(n/10)
if(x==r):
  print("{} is an Armstrong Number".format(str(x)))
  sys.exit()
print("{} is not an Armstrong Number".format(str(x)))
