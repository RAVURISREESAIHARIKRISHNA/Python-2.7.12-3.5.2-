print("Enter a number")
a=int(input())
print("Enter another number:")
b=int(input())
if(a<b):
  lcm=a
else:
  lcm=b
while(True):
  if(lcm%a==0 and lcm%b==0):
    print("LCM of {} and {} is {}".format(str(a),str(b),str(lcm)))
    break
  lcm+=1
