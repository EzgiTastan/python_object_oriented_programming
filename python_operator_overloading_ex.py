# We are improving our drawing application.
# Our application needs to support adding and comparing two Shape objects.
# Add the corresponding methods to enable addition + and comparison using the greater than > operator for the Shape class.
# The addition should return a new object with the sum of the widths and heights of the operands, while the comparison should return the result of comparing the areas of the objects.

class Shape:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width * self.height

    def __add__(self, other):
        if isinstance(other, Shape):
            # Create a new Shape object with the sum of widths and heights
            return Shape(self.width + other.width, self.height + other.height)
        else:
            raise ValueError("Cannot add Shape with non-Shape object")

    def __gt__(self, other):
        if isinstance(other, Shape):
            # Compare the areas of the two Shape objects
            return self.area() > other.area()
        else:
            raise ValueError("Cannot compare Shape with non-Shape object")


w1 = int(input())
h1 = int(input())
w2 = int(input())
h2 = int(input())

s1 = Shape(w1, h1)
s2 = Shape(w2, h2)
result = s1 + s2

print(result.area())
print(s1 > s2)

