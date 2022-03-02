class rectangle:
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth*self.length
a=int(input("Enter the length of rectangle:"))
b=int(input("Enter the breadth of rectangle:"))
obj=rectangle(a,b)
print("Area of rectangle :",obj.area())
c=int(input("Enter the length of 2nd rectangle:"))
d=int(input("Enter the breadth of 2nd rectangle:"))
obj2=rectangle(c,d)
print("Area of rectangle is:",obj2.area())
if obj.area()==obj2.area():
    print("Both equal")
elif obj.area()>obj2.area():
    print("Rectangle 1 is big")
else:
    print("Rectangle 2 is big")
print()