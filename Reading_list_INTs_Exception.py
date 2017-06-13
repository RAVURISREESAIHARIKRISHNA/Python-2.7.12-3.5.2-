def Assign(n):
  try:
    return(int(n))
  except ValueError:   # Managing Inputs Like 's'
    print("Illegal Entery\nRetry..")
    n=input()   # Asking User to Re-entry
    Assign(n)   # Calling the Same function,I correct input entered..Integer will be Returned,Else..Calling Recursively
    return(int(n)) #Returning the Appropriate Int value
  except SyntaxError:  # Managing Inputs like '5a'
    print("Illegal Entry\nRetr..") # -do-copy-
    n=input()    # -do-copy-
    Assign(n)    # -do-copy-
    return(int(n))  # -do-copy-
List=[]
print("Enter Size of the List:")
temp=input()
size=Assign(temp)
print("Size is {}".format(str(size)))
for i in range(1,size+1):
  print("Enter element {} :".format(str(i)))
  temp=input()
  List.append(Assign(temp))
print("The List is:")
print(List)
