print("\nEnter an integer:\n")
a=int(input())
print("\nEnter another integer:")
b=int(input())
i=1
while(i<=a and i<=b):
  if(a%i==0 and b%i==0):
    gcd=i
  i+=1
print("GCD of {} and {} is {}".format(str(a),str(b),str(gcd)))
