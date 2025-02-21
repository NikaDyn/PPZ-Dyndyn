print("""Створити абстрактний базовий клас (ABC) Shape з абстрактним методом area(). 
Створити клас Circle, який успадковує Shape. Властивості - radius. Функції - area(). 
Створити клас Rectangle, який успадковує Shape. Властивості - width та height. Функції - area()
""")
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width


my_circle = Circle(5)
my_rectangle = Rectangle(10, 6)

print(my_circle.area())
print(my_rectangle.area())
