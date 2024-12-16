import math


class Shape:
    def calculate_area(self):
        raise NotImplementedError("This method should be overridden by subclasses")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height


# Príklady použitia:
shapes = [
    Rectangle(5, 10),
    Circle(7),
    Triangle(6, 8)
]

for shape in shapes:
    print(f"The area of the {shape.__class__.__name__} is {shape.calculate_area()}")