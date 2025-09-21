def f1(x,y):
    print("I am in f1 Function",x+y)

def f2(a,b):
    print("I am in f2 Function")

def f3():
    pass

if __name__=="__main__":
    print("First Line")
    f1(y=12,x=15)
    print("Last Line")