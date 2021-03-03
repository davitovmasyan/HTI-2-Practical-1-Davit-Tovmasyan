import math
from datetime import datetime, date


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        if type(other) != type(self):
            raise TypeError('Cannot compare.')

        return self.radius == other.radius

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __gt__(self, other):
        return self.radius > other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

    def __repr__(self):
        return f'R={self.radius}'

    @staticmethod
    def area_formula():
        return 'π r²'

    @classmethod
    def from_perimeter(cls, p):
        # radius = p / (2 * math.pi)
        # return cls(radius)
        return cls(p / (2 * math.pi))


class Pizza(Circle):
    def __init__(self, radius, name, *ingredients):
        super(Pizza, self).__init__(radius)
        self.name = name
        self.ingredients = ingredients

    @property
    def area(self):
        return (math.pi * self.radius ** 2) * 0.9

    @classmethod
    def python(cls):
        return cls(30, 'python', 'meat', 'tomato', 'pepper')

    def __repr__(self):
        return f'<Pizza {self.name}>'


p1 = Pizza(50, 'unknown', 'mushroom', 'tomato')
print(p1)

p2 = Pizza.python()
print(p2)
# print(Circle.area_formula())
#
# c1 = Circle(10)
#
# print(c1.area_formula())
#
# # print(c1.area)
# # print(c1.perimeter)
#
# c2 = Circle(10)
# # print(c2.area)
# # print(c2.perimeter)
#
#
# print(c1 == c2 == c2)
# print(c1 > c2)
# # print(c1 == 20)
#
# # print(c1 is c2)
#
# print(Circle.from_perimeter(30))
#
# # dt = datetime(2020, 10, 10)
# # dt1 = datetime.now()
# # dt2 = date.today()
