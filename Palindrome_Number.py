import sys
print("Enter an integer:")
n=int(input())
rev=0
x=n
while(n!=0):
  rev=rev*10+n%10
  n=int(n/10)
if(rev==x):
  print("{} is a palindrome".format(str(x)))
  sys.exit()
print("{} is not a palindrome".format(str(x)))
  
