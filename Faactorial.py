def add(a,b):
  return(a+b)
items=int(input())
x=items
m=[]
while(x>=1):
  a=int(input())
  b=int(input())
  m.append([a,b])
  x=x-1
for i in range(items):
  print(m[i][0],m[i][1])
