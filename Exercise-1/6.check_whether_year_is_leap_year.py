# 6. Write a Program to find whether a given year is a leap year or not.

a = int(input("enter a year : "))
if((a % 400 == 0) or ((a % 4 == 0) and (a % 100 != 0))):
    print(a, " is a leap year")
else:
    print(a, " is not a leap year")

# This program got executed successfully and the output has been verified.
