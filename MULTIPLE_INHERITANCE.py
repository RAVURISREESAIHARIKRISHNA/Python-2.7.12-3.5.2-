"""
super() will only ever resolve a single class type for a given method, so if you're inheriting from multiple classes and want to call the method in both of them, you'll need to do it explicitly.
"""

class Test:

    def __init__(self):
        self.sub1=0
        self.sub2=0
        sefl.total=self.sub1+self.sub2
        print("Test Default Constructor Called!\n")

    def GetMarks(self):
        print("Enter Subject 1 Marks :")
        self.sub1=int(input())
        print("Enter Subject 2 Marks :")
        self.sub2=int(input())
        self.total=self.sub1+self.sub2

    def PutMarks(self):
        print("MARKS :")
        print("Subject 1 : {}\nSubject 2 : {}\nTotal : {}".format(str(self.sub1),str(self.sub2),str(self.total)))
    
    def Note1(self):
      print("TEST CLASS")


class Sports:

    def __init__(self):

        self.score=0
        print("Sports Default Constructor Called")

    def GetScore(self):
        print("Enter Sports Marks :")
        self.score=int(input())

    def PutScore(self):
        print("SPORTS\nScore : {}".format(str(self.score)))
    
    def Note1(self):
      print("SPORTS CLASS")

class Result(Test,Sports):

    def __init__(self):

        print("Result Default Constructor Called")

    def Display(self):
        self.PutMarks()
        self.PutScore()
    
    def Note1(self):
      print("RESULT CLASS")
      super().Note1() # Executes in the order in whivh inheriatance is declared Same as in C++
      Test.Note1(self) # self is Mandatory as it Require a Refernce of the Object to work on...
      Sports.Note1(self)
      
        
obj=Result()
obj.GetMarks()
obj.GetScore()
obj.Display()
print("\n\n")
obj.Note1()
