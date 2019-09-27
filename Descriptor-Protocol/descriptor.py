# Desciptor is an object attribute with a binding behavior. It's a way to create managed attributes
# Managed attributes are used to protect an attribute from change or auto update
# Python doesn't have a private variables concept. Descriptor protocol can  be considered
# as a Pythonic way to specify what happens when an attribute is referenced on a model. By use special methods
# Those method are __get__(self,obj,type=None) --> value, __set__(self,obj,value) --> None, __delete__(self,obj) --> None.
# If any of those are defined for an object, it is said to be a descriptor. In Python 2.2+
# In other programming language, descriptors are referred to setter and getter.
# let's see this code below, and image what happens
from sqlalchemy import Column, Integer, String


class User:
    id = Column(Integer, primary_key=True)
    name = Column(String)

# If you ever wonder why don't use __init__() method to initialize for id and 
# name bind to the instances like regular classes do.
# In Python, there are three ways to access attribute a of the object obj.
# 1. some_variable=obj.a; 2. obj.a=some_value; 3. del obj.a
# Why you want to use descriptors?
# example:
# class FoodOrder:

#     def __init__(self,name,price,quantity):
#         self._name=name
#         self._price=price
#         self._quantity=quantity

#     def getTotal(self):
#         return self._price*self._quantity

# noodle=FoodOrder("Beef Noodle",45000,2)
# print(noodle.getTotal()) # OK, print 90000 here
# # But now we try to change the atttributes
# noodle._quantity=-2 # that's ok, but in fact, that's a bug
# print(noodle.getTotal()) # -90000

# Instead of using getter and setter method to enforce _quantity be positive
# class FoodOrder:
#     def __init__(self,name,price,quantity):
#         self._name=name
#         self._price=price
#         self._quantity=quantity

#     @property
#     def quantity(self):
#         return self._quantity
#     @quantity.setter
#     def quantity(self,value):
#         if value<0:
#             raise ValueError("Value must be positve")
#         self._quantity=value

# tea=FoodOrder("Tea",20000,2)
# # tea.quantity=-2 # will raise error here
# tea.quantity=3 # that's OK
# Actually, in this example above, price attribute can be negative, we must fix that
# But we don't want to repeat the same things we do with quantity attribute to price (it's DRY principle)
# So, we must use descriptors
# When you call obj.attribute_name, Python will cause your object to look attribute_name
# in obj. If attribute_name happens to define __get__(), then attribute_name.__get__(obj)
# will get call. 




class NonNegative:
    # If use __set_name(self,owner,name), we need to remove __init__()

    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Value must be positive")
        instance.__dict__[self.name] = value
    
    # in Python 3.6+. We use new API obj.__set_name(self,owner,name) like below
    # And does not need __init__() method

    # def __set_name__(self, name):
    #     self.name = name


class FoodOrder():
    price = NonNegative('price')
    quantity = NonNegative('quantity')
    # If use __set_name__, it'll look like below
    # price = NonNegative()
    # quantity = NonNegative()

    def __init__(self, name, price, quantity):
        self._name = name
        self.price = price
        self.quantity = quantity

    def getTotal(self):
        return self.price * self.quantity


rice = FoodOrder('rice', 30000, 3)
rice.getTotal()  # 90000

rice.price = -10000  # ValueError
rice.quantity = -4  # ValueError
