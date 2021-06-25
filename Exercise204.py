class Rectangle():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)


class Cube():
    def __init__(self, square: Square):
        self.square = square
        self.height = self.square.a

    def areaC(self):
        return self.square.area()

    def volume(self):
        return self.square.area() * self.height


class Cuboid():
    def __init__(self, figure, height):
        self.figure = figure
        self.height = height

    def volume(self):
        return self.figure.area() * self.height


kwadrat = Square(6)
print(kwadrat.a)
print(kwadrat.b)
print(kwadrat.area())

szescian = Cube(kwadrat)
print(szescian.areaC())
print(szescian.volume())

print(Cuboid(Rectangle(5, 4), 6).volume())
