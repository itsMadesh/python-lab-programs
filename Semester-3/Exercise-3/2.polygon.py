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

# import math
# from abc import ABC, abstractmethod 
# class Polygon(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def perimeter(self):
#         pass
# class Triangle(Polygon):
#     # Triangle has 3 sides|Area=½ x (base) x (height)|Perimeter=a+b+c
# class IsoscelesTriangle(Triangle):
#     # IsoscelesTriangle has 3 sides|Area=(b*h)/2|Perimeter=2*a+b
#     # Any two sides are equal
# class EquilateralTriangle(Triangle):
#     a=int(input("Enter side(in cm) for equilateral triangle:"))
#     # EquilateralTriangle has 3 sides|Area=(sqrt(3)/4)*a^2|Perimeter=3*a
#     # All sides are equal
# class Quadrilateral(Polygon):
#     # Quadrilateral has 4 sides|Area=1/2 x diagonals length x ( sum of the height of two triangles )|Perimeter = AB + BC + CD + DA
# class Rectangle(Quadrilateral):
#     l=int(input("Enter length(in cm) of a triangle:"))
#     b=int(input("Enter breadth(in cm) of a triangle:"))
#     # Rectangle has 4 sides|Area=Length x Breadth|Perimeter=2(length+breadth)
# class Square(Quadrilateral):
#     a=int(input("Enter square side in cm:"))
#     # Square has 4 sides|Area=side^2|Perimeter=4(side)
# class Pentagon(Polygon):
#     a=int(input("Enter pentagon side in cm:"))
#     # Pentagon has 5 sides|Area=(1/4)sqrt(5(5+2*sqrt(5)*side^2)|Perimeter=5a
# class Hexagon(Polygon):
#     a=int(input("Enter hexagon side in cm:"))
#     # Hexagon has 6 sides|Area=(3*sqrt(3)/2)*side^2|Perimeter=6a
# class Octagon(Polygon):
#     a=int(input("Enter octagon side in cm:"))
#     # Octagon has 7 sides|Area=2*a^2(1+sqrt(2))|Perimeter=8a


from abc import ABC, abstractmethod  # need these definitions


class Polygon(ABC):

    def __init__(self, lengths_of_sides):
        self.number_of_sides = len(lengths_of_sides)
        self.lengths_of_sides = [0] * self.number_of_sides
        self.assign_values_to_sides(lengths_of_sides)
    
    def print_num_sides(self):
        """a quick, informational print statement"""
        print('There are ' + str(self.number_of_sides) + 'sides.')
        
    def assign_values_to_sides(self, lengths_of_sides):
        index = 0
        while index < len(lengths_of_sides):
            self.lengths_of_sides[index] = lengths_of_sides[index]
            index += 1

    @abstractmethod
    def area(self):
        """Return the area of the polygon."""
        pass
        
    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the polygon."""
        pass


class Triangle(Polygon):

    def __init__(self, lengths_of_sides):
        super().__init__(lengths_of_sides)
        assert 3, self.number_of_sides

    def area(self):
        """return the area of the triangle using the semi-perimeter method"""
        a, b, c = self.lengths_of_sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        return (s*(s-a)*(s-b)*(s-c)) ** 0.5
    
    def perimeter(self):
        """Return the perimeter of the polygon."""        
        # calculate the perimeter
        s = (self.lengths_of_sides[0] + self.lengths_of_sides[1] + self.lengths_of_sides[2])
        return s


class IsoscelesTriangle(Triangle):

    def __init__(self, side, base):  # [side, base]
        super().__init__([side, side, base])


class EquilateralTriangle(Triangle):

    def __init__(self, side):  # side
        super().__init__([side, side, side])

        
class Pentagon(Polygon):

    def __init__(self, lengths_of_sides):
        super().__init__(lengths_of_sides)
        assert 5, self.number_of_sides
    
    def area(self):
        x, y = self.lengths_of_sides[0], self.lengths_of_sides[1]
        return x * y

    def perimeter(self):
        """Return the perimeter of the polygon."""        
        # calculate the perimeter
        x, y = self.lengths_of_sides
        return (x+y)*2

        
class Hexagon(Polygon):

    def __init__(self, lengths_of_sides):
        super().__init__(lengths_of_sides)
        assert 6, self.number_of_sides

    def area(self):
        x, y = self.lengths_of_sides[0], self.lengths_of_sides[1]
        return x * y

    def perimeter(self):
        """Return the perimeter of the polygon."""        
        # calculate the perimeter
        x, y = self.lengths_of_sides
        return (x+y)*2


class Octagon(Polygon):

    def __init__(self, lengths_of_sides):
        super().__init__(lengths_of_sides)
        assert 8, self.number_of_sides

    def area(self):
        x, y = self.lengths_of_sides[0], self.lengths_of_sides[1]
        return x * y

    def perimeter(self):
        """Return the perimeter of the polygon."""        
        # calculate the perimeter
        x, y = self.lengths_of_sides
        return (x+y)*2


class Quadrilateral(Polygon):

    def __init__(self, lengths_of_sides):  # [side1, side2]
        super().__init__([lengths_of_sides[0], lengths_of_sides[1], lengths_of_sides[0], lengths_of_sides[1]])
        assert 4, self.number_of_sides

    def area(self):
        x, y = self.lengths_of_sides[0], self.lengths_of_sides[1]
        return x * y

    def perimeter(self):
        """Return the perimeter of the polygon."""        
        # calculate the perimeter
        x, y = self.lengths_of_sides
        return (x + y) * 2
    
        
class Rectangle(Quadrilateral):

    def __init__(self, lengths_of_sides):  # [side1, side2]
        super().__init__(lengths_of_sides)
    
    def area(self):
        x, y = self.lengths_of_sides[0], self.lengths_of_sides[1]
        return x * y

    def perimeter(self):
        """Return the perimeter of the polygon."""        
        # calculate the perimeter
        x, y = self.lengths_of_sides
        return (x + y) * 2

    
class Square(Rectangle):

    def __init__(self, side):  
        super().__init__([side, side])
    
    def area(self):
        x = self.lengths_of_sides[0]
        return x * x

    def perimeter(self):
        """Return the perimeter of the polygon."""        
        # calculate the perimeter
        x = self.lengths_of_sides[0]
        return x * 4
print(Pentagon([3,5]))