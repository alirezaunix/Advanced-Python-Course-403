class Person:
    fname=""
    lname=""
    age=0
    
    def sleeping(self):
        print("I am sleeping")
    
    def walking(self):
        print("I am walking")
        

p1=Person()

#1
p1.age=12
print(p1.age)
#2
setattr(p1,"age",12)
print(getattr(p1,"age"))