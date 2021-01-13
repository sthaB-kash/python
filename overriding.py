import math


class Shape:
    def __init__(self, name):
        self.name = name

    def fact(self):
        print("I'm two dimensional shape")

    def __str__(self):
        return self.name


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        print("area= ", math.pi*self.radius**2)

    def fact(self):
        pass


C = Circle(3.3)
print(C.fact())
print(C)

x, y, z = (2, 3, 4)


def add(a, b, c: int = 0):
    print("sum: ", a+b+c)


add(x, y)
add(x, y, z)
