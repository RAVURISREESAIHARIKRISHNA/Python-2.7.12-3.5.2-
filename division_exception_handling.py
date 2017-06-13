def Divide(a,b):
  try:
    return (a/b)
  except ZeroDivisionError:
    print("\nHey!Dont be insane!\n")

print("\nEnter Numerator:\n")
num=float(input())
print("\nEnter Denominator:\n")
den=float(input())
ans=Divide(num,den)
if(ans!=None):
  print("\nAnswer is : "+str(ans))
