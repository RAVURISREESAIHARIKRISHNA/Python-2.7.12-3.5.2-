class Employee:
 
  def __init__(self,name="",EmpNo=0):  #Default Values as CONSTRUCTOR CANNOT BE OVERLOADED
    self.name=name
    self.EmpNo=EmpNo
    print("Parameterized Constructor Called")
  def Display(self):
    print("Employee Name : "+self.name+"\nEmployee Name : "+str(self.EmpNo))
  def SetData(self,name,EmpNo):
    self.name=name
    self.EmpNo=EmpNo
    print("Details Setted!")
    self.Display()


print("Initilization With Direct Constructor :")
emp1=Employee("Hari",315506408038)
emp1.Display()
print("Assigning With User Input:")
print("Enter Name of The Employee:")
name=input()
print("Enter Employee Number:")
EmpNo=int(input())
obj2=Employee()
print("\n\nAfter Setting With Default Values:......\n\n")
obj2.Display()
obj2.SetData(name,EmpNo)
#obj2.name="Hacked"
#obj2.Display()
