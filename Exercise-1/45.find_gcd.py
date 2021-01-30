# 45. Write a function GCD (greatest common divisor) that accepts two integers and returns -1 if both the
# integers are zero, otherwise it returns their GCD.

a = int(input("Enter a number a :"))
b = int(input("Enter a number b :"))


def find_gcd(a, b):
    if a == 0 and b == 0:
        return -1
    gcd = 1
    for i in range(2, min(a, b)+1):
        if(a % i == 0 and b % i == 0):
            gcd = i
    return gcd


print("Gcd of", a, "and", b, " is", find_gcd(a, b))

# This program got executed successfully and the output has been verified.
