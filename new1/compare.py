class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

def compare_rectangles(rect1, rect2):
    area1 = rect1.area()
    area2 = rect2.area()

    if area1 > area2:
        return "Rectangle 1 is larger."
    elif area1 < area2:
        return "Rectangle 2 is larger."
    else:
        return "Both rectangles have the same area."

length1 = float(input("Enter the length of Rectangle 1: "))
breadth1 = float(input("Enter the breadth of Rectangle 1: "))
rectangle1 = Rectangle(length1, breadth1)

length2 = float(input("Enter the length of Rectangle 2: "))
breadth2 = float(input("Enter the breadth of Rectangle 2: "))
rectangle2 = Rectangle(length2, breadth2)

result = compare_rectangles(rectangle1, rectangle2)

print(result)
