# 9. Write a Program to find the largest of three numbers.

a = int(input("Enter a first number :"))
b = int(input("Enter a second  number :"))
c = int(input("Enter a third number :"))
if(a > b and a > c):
    print(a, "is largest ")
elif(b > a and b > c):
    print(b, "is largest ")
else:
    print(c, "is largest ")

# This program got executed successfully and the output has been verified.
