def Prime(n):
  y=2
  count=0
  while(y<n):
    if(n%y==0):
      count=1
      break
    else:
      y+=1
  if(count==0):
    return 1
  else:
    return 0
print("Enter an integer:\n")
n=int(float(input()))              #int(19.5) can't be converted to 19.So converting "19.5" to 19.5 and then to 19
x=Prime(n)
if(x==1):
  print("\n"+str(n)+" is a prime number")
else:
  print("\n"+str(n)+" is not a prime")
exit()
