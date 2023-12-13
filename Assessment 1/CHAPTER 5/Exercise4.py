import tkinter as tk
import math

class Shape:
    def __init__(self):
        self.sides = []

    def inputSides(self):
        pass

    def area(self):
        pass

class Circle(Shape):
    def inputSides(self):
        radius = float(input("Enter the radius of the circle: "))
        self.sides.append(radius)

    def area(self):
        return math.pi * (self.sides[0] ** 2)

class Rectangle(Shape):
    def inputSides(self):
        length = float(input("Enter the length of the rectangle: "))
        breadth = float(input("Enter the breadth of the rectangle: "))
        self.sides.extend([length, breadth])

    def area(self):
        return self.sides[0] * self.sides[1]

class Triangle(Shape):
    def inputSides(self):
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        self.sides.extend([base, height])

    def area(self):
        return 0.5 * self.sides[0] * self.sides[1]

def calculate_area(shape):
    shape.inputSides()
    area = shape.area()
    output_label.config(text=f"Area: {area}")

root = tk.Tk()
root.title("Area Calculator")

shape_label = tk.Label(root, text="Select a Shape:")
shape_label.pack()

circle_button = tk.Button(root, text="Circle", command=lambda: calculate_area(Circle()))
circle_button.pack()

rectangle_button = tk.Button(root, text="Rectangle", command=lambda: calculate_area(Rectangle()))
rectangle_button.pack()

triangle_button = tk.Button(root, text="Triangle", command=lambda: calculate_area(Triangle()))
triangle_button.pack()

output_label = tk.Label(root, text="")
output_label.pack()

root.mainloop()