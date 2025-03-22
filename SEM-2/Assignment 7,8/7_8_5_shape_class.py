""" Create a base class "Shape" with methods to calculate the area and perimeter. 
Implement derived classes "Rectangle" and "Circle" that inherit from "Shape" and provide their own area and perimeter calculations. """

import math

class Shape:
    def area(self):
        pass

    def peri(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def peri(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def peri(self):
        return 2 * math.pi * self.radius

while True:
    choice = int(input("\nEnter your Choice :--\n1 - Rectangle\n2 - Circle\n3 - Exit\nChoice : "))
    match choice:
        case 1:
            length = float(input("Enter Length of Rectangle : "))
            width = float(input("Enter Width of Rectangle : "))
            rect = Rectangle(length, width)
            print("Area of the Rectangle :", rect.area())
            print("Perimeter of the Rectangle :", rect.peri())
        case 2:
            radius = float(input("Enter Radius of Circle : "))
            circ = Circle(radius)
            print("Area of the Circle:", circ.area())
            print("Perimeter of the Circle :", circ.peri())
        case 3:
            break
        case _:
            print("INVALID CHOICE - TRY AGAIN.")