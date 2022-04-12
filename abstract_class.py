
# from abc import ABCMeta, abstractmethod
from abc import ABC, abstractmethod
#Abstract method is defined under two modules ABCMeta and ABC
#if a base class method is defined as abstract method
#then it is necessary for derived classes to have same method
class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth

rect1 = Rectangle()
print(rect1.printarea())
#sh=Shape()
#we can't make object of class having abstract method here it is Shape class
