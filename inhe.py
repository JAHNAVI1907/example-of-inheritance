class add:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("Addition is also initiallised by receiving a,b from obj")
    def addition(self):
        return self.a+self.b
class mul:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("multiplication is also intialised by receiving a,b from obj")
    def multiplication(self):
        return self.a*self.b
class calc(add,mul):
    def __init__(self,a,b):
        add.__init__(self,a,b)
        mul.__init__(self,a,b)
        print("calci class initialized")
x=int(input("enter the value of a:"))
y=int(input("enter the value of b:"))
c=calc(x,y)
print("sum =",c.addition())
print("multiplication =",c.multiplication())
