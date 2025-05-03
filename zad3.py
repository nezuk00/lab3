from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


def print_shape_info(shape):
    print(f"Тип фигуры: {shape.__class__.__name__}")
    print(f"Площадь: {shape.area():.2f}")
    print(f"Периметр: {shape.perimeter():.2f}")
    print()



if __name__ == "__main__":

    rectangle = Rectangle(5, 10)
    circle = Circle(7)
    triangle = Triangle(3, 4, 5)


    print_shape_info(rectangle)
    print_shape_info(circle)
    print_shape_info(triangle)