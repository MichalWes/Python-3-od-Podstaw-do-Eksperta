class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)


class Cube(Square):
    def areaC(self):
        return super().area() * 6

    def volume(self):
        return super().area() * self.a


kwadrat = Square(6)
print(kwadrat.a)
print(kwadrat.b)
print(kwadrat.area())

szescian = Cube(4)
print(szescian.areaC())
print(szescian.volume())
