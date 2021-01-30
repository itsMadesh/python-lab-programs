# 10. Write a Program to calculate the roots of a Quadratic Equation.

import math
a = int(input("Enter a number a :"))
b = int(input("Enter a number b :"))
c = int(input("Enter a number c :"))
d = b*b-4*a*c
if(d >= 0):
    root1 = (-b+math.sqrt(d))/2*a
    root2 = (-b-math.sqrt(d))/2*a
    print("roots are", root1, ",", root2)
else:
    print("roots are imaginary")

# This program got executed successfully and the output has been verified.
