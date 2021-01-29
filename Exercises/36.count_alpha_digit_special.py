# 36. Write a program to count total number of alphabets, digits and special characters in a string.

x = input("Enter a string : ")
a, d, s = 0, 0, 0
for c in x:
    if c.isalpha():
        a = a+1
    elif c.isdigit():
        d = d+1
    else:
        s = s+1
print("No of alphabets : ", a)
print("No of digits : ", d)
print("No of special chars : ", s)

# This program got executed successfully and the output has been verified.
