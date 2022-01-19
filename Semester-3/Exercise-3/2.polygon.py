# 2. Develop an inheritance hierarchy based upon a Polygon class that has abstract
# methods area () and perimeter (). Implement classes Triangle, Quadrilateral,
# Pentagon, Hexagon, and Octagon that extend this base class, with the obvious
# meanings for the area () and perimeter () methods. Also implement classes,
# IsoscelesTriangle, EquilateralTriangle, Rectangle, and Square, that have the
# appropriate inheritance relationships. Finally, write a simple program that allows
# users to create polygons of the various types and input their geometric
# dimensions, and the program then outputs their area and perimeter. For extra
# effort, allow users to input polygons by specifying their vertex coordinates and be
# able to test if two such polygons are similar.

from abc import ABC, abstractmethod
class Polygon(ABC):
    def areaandperi(self):
        pass
class Triangle(Polygon):
    def __init__(self,a,b,c):
        self.a,self.b,self.c=a,b,c
        s=self.a+self.b+self.c
        print("Perimeter:",self.a+self.b+self.c)
        print("Area:",((s)*(s-self.a)*(s-self.b)*(s-self.c))**(0.5))
class Quadrilateral(Polygon):
    def __init__(self,base,side):
        self.base=base
        self.side=side
        print("Area=",self.base*self.side,"Perimeter=",2*(self.base+self.side))
class pentagon(Polygon):
    def __init__(self,a):
        self.a=a
        print("Perimeter:",5*a)
        print(round("Area=",(0.25*((5*(5+4))**1/2))*(self.a**2)))
class hexagon(Polygon):
    def __init__(self,a):
        self.a=a
        print((1.5*1.732)*(self.a**2))
class Rectangle(Quadrilateral): 
    def __init__(self, base, side):
        super(Rectangle, self).__init__(base,side)
class Square(Quadrilateral): 
    def __init__(self, base,side):
        super(Square, self).__init__(base,side)
class isostri(Triangle):
    def __init__(self, base,side,side2):
        super(isostri, self).__init__(base,side,side2)
class equitri(Triangle):
    def __init__(self, base,side2):
        super(equitri, self).__init__(base,side2)
print("perimeter and area of square of sides are length of 44cm,30cm:")
d=Square(44,30)
