class Rectangle:
    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth

    def get_length(self):
        return self.__length

    def get_breadth(self):
        return self.__breadth

    def area(self):
        return self.get_length() * self.get_breadth()

    def __lt__(self, ob):
        if self.area() < ob.area():
            return True
        else:
            return False

# main
l1 = int(input("enter length 1: "))
b1 = int(input("enter breadth 1: "))
ar1 = Rectangle(l1, b1)
l2 = int(input("\nenter length 2: "))
b2 = int(input("enter breadth 2: "))
ar2 = Rectangle(l2, b2)

print("area of rectangle 1: ", ar1.area())
print("area of rectangle 2: ", ar2.area())

if ar1 < ar2:
    print("First rectangle is small")
else:
    print("Second rectangle is small")
