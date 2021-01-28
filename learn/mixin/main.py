# super() deep dive
# mechanism of super()
# super() can also take two parameter:
# the first is the subclass, the second is an object that is an instance of
# that subclass


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length * self.width


class Square(Rectangle):
    def __init__(self, length):
        super(Square, self).__init__(length, length)


# class Cube(Square):
#     def surface_area(self):
#         face_area = super(Square, self).area()
#         return face_area * 6

#     def volume(self):
#         face_area = super(Square, self).area()
#         return face_area * self.length


sq = Square(10)
print(sq.area(), sq.perimeter(), sep="\n")
# cu = Cube(20)
# print(cu.volume(), cu.surface_area(), sep="\n")
# the above example setting Square as the subclass argument to super(), instead
# of Cube. This causes super() to start searching for a matching method.

# super() in multiple inheritance


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class RightPyramid(Triangle, Square):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height
        super().__init__(self.base)  # the right way to calculate area()

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area


# pyramid = RightPyramid(2, 4)
# print(pyramid.area())  # AttributeError here. because the method resolution order

# MRO
# MRO tells Python how to search for inherited methods.
# this comes in handy when you're using super() because the MRO tells you
# exactly wher Python will look for a method you're calling with super() and in
# what order

print(RightPyramid.__mro__)
# super() will be searched first in RightPyramid, then in Triangle, then in
# Square, then in Rectangle. if nothing is found, in object from which all
# classes originate


# Multiple inheritance alternative - mixin
class VolumeMixin:
    def volume(self):
        return self.area() * self.height


class Cube(VolumeMixin, Square):
    def __init__(self, length):
        super().__init__(length)
        self.height = length

    def face_area(self):
        return super().area()

    def surface_area(self):
        return super().area() * 6


test = Cube(10)
print(test.area(), test.face_area(), test.surface_area(), test.volume(), sep="\n")
