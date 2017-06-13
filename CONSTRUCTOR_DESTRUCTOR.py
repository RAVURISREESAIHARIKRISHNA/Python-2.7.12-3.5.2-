class Test:
  
  def __init__(self):
    
    print("Constructor Called")
    
  def __del__(self):
    print("Destructor Called")

o=Test()
p=o
print id(p)
print id(o)
del o
del p
