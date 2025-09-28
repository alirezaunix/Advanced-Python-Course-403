class Person:

    def __init__(self,fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.age=age
                
    def sleeping(self):
        print("I am sleeping")
    
    def walking(self):
        print("I am walking")
    
    def showInfo(self):
        print(f"Firstname is {self.fname} and Lastname is {self.lname} and Age is {self.age}")

class Student(Person):
    def __init__(self,fname,lname,age,ID):
        super.__init__(self,fname,lname,age)
        self.ID=ID


s1=Student("reza","gholi",23,123)
s1.showInfo()