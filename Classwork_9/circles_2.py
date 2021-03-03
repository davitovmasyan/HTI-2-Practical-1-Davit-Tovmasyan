import math
from datetime import datetime, date


class Circle:
    PI = 3.14
    area_formula = 'π r²'

    def __init__(self, radius):
        # self.radius = radius
        self._radius = radius  # current and children
        # self.radius = radius
        # self.__radius = radius  # only current class

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        type_of_value = type(value)
        if not (type_of_value == int or type_of_value == float):
            raise TypeError(f'Radius must be int or float, not {type_of_value}')

        self._radius = value

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
        return self.PI * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * self.PI * self.radius

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


c1 = Circle(10)
print(c1.PI)
print(Circle.PI)
# c1.radius
# c1._radius = 'abc'  # we are all adults
# c1.Circle__radius = 'abc'  # mangle
# c1.__radius = 'abc'  # mangle

print(c1.area)
# p1 = Pizza(50, 'unknown', 'mushroom', 'tomato')
# print(p1)
#
# p2 = Pizza.python()
# print(p2)
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

# print('-'*80)
#
# print(getattr(c1, 'radius'))  # c1.radius
#
# # print(getattr(c1, 'blabla'))  # exception
# print(getattr(c1, 'blabla', None))
# print(getattr(c1, 'radius', None))
#
# setattr(c1, 'blabla', 'foo')
# print(c1.blabla)
# print(hasattr(c1, 'blabla'))


# bad thing
# class Foo:
#     def __init__(self, **kwargs):
#         for key, value in kwargs.items():
#             setattr(self, key, value)
#
#
# f = Foo(a=1, b='xyz', c=[1, 2, 3])
# print(f.a)
# print(f.b)
# print(f.c)


# int() bool()

# print(issubclass(bool, int))
# print(isinstance(True, int), 'foo')
