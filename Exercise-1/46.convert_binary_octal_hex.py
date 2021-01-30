# 46. Convert the given decimal number into binary, octal and hexadecimal numbers using user defined functions.

n = int(input("Enter a number : "))


def bin(n):
    s = ""
    while(n):
        s = str(n % 2)+s
        n = n//2
    return s


def oct(n):
    s = ""
    while(n):
        s = str(n % 8)+s
        n = n//8
    return s


def hex(n):
    s = ""
    while(n):
        rem = n % 16
        c = rem if rem < 10 else chr(55+rem)
        s = str(c)+s
        n = n//16
    return s


print("Binary of ", n, " is ", bin(n))
print("Octal of ", n, " is ", oct(n))
print("Hexadecimal of ", n, " is ", hex(n))

# This program got executed successfully and the output has been verified.
