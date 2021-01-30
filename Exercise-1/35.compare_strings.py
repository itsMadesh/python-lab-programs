# 35. Write a program to compare two string without using string library functions.

x = input("Enter string-1 : ")
y = input("Enter string-2 : ")


def compare(x, y):
    if(len(x) != len(y)):
        return False
    for i in range(len(x)):
        if(x[i] != y[i]):
            return False
    return True


if(compare(x, y)):
    print("Both strings are equal")
else:
    print("Both strings are not equal")

# This program got executed successfully and the output has been verified.
