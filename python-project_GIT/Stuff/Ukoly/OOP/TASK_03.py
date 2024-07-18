import json

class Shape:
    def __init__(self, shape_type):
        self.shape_type = shape_type

    def Show(self):
        raise NotImplementedError("Subclasses should implement this method")

    def Save(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.__dict__, file)

    @classmethod
    def Load(cls, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            shape_type = data.pop('shape_type')
            shape_class = globals()[shape_type]
            return shape_class(**data)


class Square(Shape):
    def __init__(self, x, y, side_length):
        super().__init__('Square')
        self.x = x
        self.y = y
        self.side_length = side_length

    def Show(self):
        print(f"Square: Upper left corner ({self.x}, {self.y}), Side length {self.side_length}")


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__('Rectangle')
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def Show(self):
        print(f"Rectangle: Upper left corner ({self.x}, {self.y}), Width {self.width}, Height {self.height}")


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__('Circle')
        self.x = x
        self.y = y
        self.radius = radius

    def Show(self):
        print(f"Circle: Center ({self.x}, {self.y}), Radius {self.radius}")


class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        super().__init__('Ellipse')
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def Show(self):
        print(f"Ellipse: Upper left corner ({self.x}, {self.y}), Width {self.width}, Height {self.height}")


# Create a list of shapes
shapes = [
    Square(1, 2, 5),
    Rectangle(2, 3, 4, 5),
    Circle(3, 4, 6),
    Ellipse(4, 5, 7, 8)
]

# Save the shapes to a file
for i, shape in enumerate(shapes):
    shape.Save(f'shape_{i}.json')

# Load the shapes into another list
loaded_shapes = []
for i in range(len(shapes)):
    loaded_shape = Shape.Load(f'shape_{i}.json')
    loaded_shapes.append(loaded_shape)

# Display information about each loaded shape
for shape in loaded_shapes:
    shape.Show()