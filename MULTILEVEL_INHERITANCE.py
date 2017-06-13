class Student:
  
  def __init__(self):
    print("Student Default Constructor")
    self.Name=""
    self.Roll=0
    
  def GetDetails(self):
    print("Enter Name of the Student :")
    self.Name=input()
    print("Enter Roll Number :")
    self.Roll=int(input())
  
  def PutDetails(self):
    print("Studen Name : {}\nRoll Number : {}".format(self.Name,str(self.Roll)))
  
class Test(Student):
  
  def __init__(self):
    print("Test Default Constructor")
    self.sub1=0
    self.sub2=0
    self.total=self.sub1+self.sub2
    
  def GetMarks(self):
    print("Enter Sub1 Marks :")
    self.sub1=int(input())
    print("Enter Sub2 MArks :")
    self.sub2=int(input())
    self.total=self.sub1+self.sub2
  
  def PutMarks(self):
    print("\nSub 1 : {}\nSub2 : {}\nTotal : {}".format(str(self.sub1),str(self.sub2),str(self.total)))
  
class Sports(Test):
  
  def __init__(self):
    print("SPORTS Default Constructor")
    self.Score=0
  
  def GetScore(self):
    print("Enter Sports MArks :")
    self.Score=int(input())
  
  def Display(self):
    self.PutDetails()
    self.PutMarks()
    print("Sports : {}".format(str(self.Score)))

obj=Sports()
obj.GetDetails()
obj.GetMarks()
obj.GetScore()
obj.Display()
