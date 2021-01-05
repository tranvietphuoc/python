# Python support inheritance from multiple classes. This part will show you:
# how multiple inheritance works
# how to use super() to call methods inherited from multiple parents
# what complexities derive from multiple inheritance
# how to write a mixin, which is a common use of multiple inheritance


class RightPyramid(Triangle, Square):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height

    def what_am_i(self):
        return "Pyramid"


# The Method Resolution Order (MRO) dertermines where Python looks for a method when there is
# hierrachy of classes.


class A:
    def __init__(self):
        print("A")
        super().__init__()


class B(A):
    def __init__(self):
        print("B")
        super().__init__()


class X:
    def __init__(self):
        print("X")
        super().__init__()


class Forward(B, X):
    def __init__(self):
        print("Forward")
        super().__init__()


class Backward(X, B):
    def __init__(self):
        print("Backward")
        super().__init__()


# If you combine the MRO and the **kwargs feature for specifying name-value pairs during
# construction, you can write code that passes parameters to parent classes even if they have
# different name


class Rectangle:
    def __init__(self, length, width, **kwargs):
        self.length = length
        self.width = width
        super().__init__(**kwargs)

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


class Square(Rectangle):
    def __init__(self, length, **kwargs):
        super().__init__(length=length, width=length, **kwargs)


class Triangle:
    def __init__(self, base, height, **kwargs):
        self.base = base
        self.heigth = height
        super().__init__(**kwargs)

    def tri_area(self):
        return 0.5 * self.base * self.length


class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height, *kwargs):
        self.base = base
        self.slant_height
        kwargs["height"] = slant_height
        kwargs["length"] = base
        super().__init__(base=base, **kwargs)

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area

    def area_2(self):
        base_area = super().area()
        triangle_area = super().tri_area()
        return triangle_area * 4 + base_area


# Multiple inheritance can get tricky quickly. A simple use case that is common in the field is to
# write a mixin. A mixin is a class that doesn't care about its position in the hierrachy, but just
# provides one or more convenience methods


class SurfaceMixin:
    def surface_area(self):
        surface_area = 0
        for surface in self.surfaces:
            surface_area += surface.area(self)

        return surface_area


class Cube(Square, SurfaceMixin):
    def __init__(self, length):
        super().__init__()
        self.surfaces = [Square, Square, Square, Square, Square, Square]


class RightPyramid(Square, Triangle, SurfaceMixin):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height
        self.height = base
        self.width = base

        self.surfaces = [Square, Triangle, Triangle, Triangle, Triangle]
