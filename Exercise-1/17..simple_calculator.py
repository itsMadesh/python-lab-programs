# 17. Write a program for a simple calculator.

while(True):
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.exit")
    c = int(input("Enter a choice no:"))
    if(c < 1 or c > 5):
        print(" Invalid input ")
        continue
    elif(c == 5):
        break
    a = float(input("Enter a number a : "))
    b = float(input("Enter a number b : "))
    if(c == 1):
        print(a, "+", b, "=", a+b)
    elif(c == 2):
        print(a, "-", b, "=", a-b)
    elif(c == 3):
        print(a, "*", b, "=", a*b)
    elif(c == 4):
        print(a, "/", b, "=", a/b)

# This program got executed successfully and the output has been verified.
