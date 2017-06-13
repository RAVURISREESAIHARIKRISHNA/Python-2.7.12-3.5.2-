#*********** HIEARARCHIAL INHERITANCE  ******************


class Person:
  
  def GetName(self):
    print("Enter Name of the Person :")
    self.Name=input()
  
  def GetSex(self):
    print("Enter Sex :")
    self.Sex=input()
    
class Student(Person):
  
  def GetCollege(self):
    print("Enter College Name :")
    self.ClgName=input()
  
  def GetMarks(self):
    print("Enter Total Marks:")
    self.Marks=int(input())
    
  def Student_Display(self):
    print("Student Name : "+self.Name)
    print("Sex : "+self.Sex)
    print("College Name : "+self.ClgName)
    print("Total Marks : "+str(self.Marks)+"\n\n")
    
class Employee(Person):
  
  def GetCompany(self):
    
    print("Enter Company Name :")
    self.CompName=input()
    
  
  def GetBasic(self):
    print("Enter Basic Salary :")
    self.Basic=int(input())
    
  def Employee_Display(self):
    print("Employee Name : "+self.Name)
    print("Sex : "+self.Sex)
    print("Company Name : "+self.CompName)
    print("Basic Salary : "+str(self.Basic)+"\n\n")

objs=Student()
objs.GetName()
objs.GetSex()
objs.GetCollege()
objs.GetMarks()
objs.Student_Display()


obje=Employee()
obje.GetName()
obje.GetSex()
obje.GetCompany()
obje.GetBasic()
obje.Employee_Display()
