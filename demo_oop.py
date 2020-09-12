class MyClass:
    def method(self):
        return "instance method called", self

    @classmethod
    def classmethod(cls):
        return "class method called", cls
    
    @staticmethod
    def staticmethod():
        return "static method called"


#obj = MyClass()
#print(obj.method())
#print(obj.classmethod())
#rint(obj.staticmethod())

#print(MyClass.classmethod())
#print(MyClass.staticmethod())
#print(MyClass.method())  --> Error

import math

class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza({self.radius!r}, '
                f'{self.ingredients!r})')

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi


#print(Pizza(['cheese', 'tomatoes']))
#print(Pizza.margherita())
#print(Pizza.prosciutto())

p = Pizza(4, ['mozzarella', 'tomatoes'])
print(p)
print(p.area())
Pizza.circle_area(4)