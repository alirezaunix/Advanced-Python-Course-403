class Person:
    fname=""
    lname=""
    age=0
    
    def sleeping(self):
        print("I am sleeping")
    
    def walking(self):
        print("I am walking")
        

p1=Person()
print(id(p1))

p2=Person()
print(id(p2))
