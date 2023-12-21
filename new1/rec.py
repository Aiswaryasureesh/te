class Rectangle:
    def getdata(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def display(self):
        ar=self.length * self.breadth
        print("area : ",ar)
    
    def perimeter(self):
        pr=2 * (self.length+self.breadth)
        print("perimeter : ",pr)

l=int(input("enter length "))
b=int(input("enter breadth "))
ob=Rectangle()
ob.getdata(l,b)
ob.display()
ob.perimeter()
