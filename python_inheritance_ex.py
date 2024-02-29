# You are making a drawing application, which has a Shape base class.
# 1. Inherit the Rectangle class from Shape.
# 2. Define the perimeter() method in the Rectangle class, printing the perimeter of the rectangle.
# The perimeter is equal to 2*(width+height)
# solution:

# base class
class Shape:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        print(self.width * self.height)

# Rectangle class inherits from Shape
class Rectangle(Shape):
    def perimeter(self):
        print(2 * (self.width + self.height))

# Getting input for width and height
w = int(input())
h = int(input())

# Creating an instance of Rectangle
r = Rectangle(w, h)

# Calling area and perimeter methods
r.area()
r.perimeter()