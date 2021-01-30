# 33. Write a program to check if a string is a palindrome.

s = input("Enter a string : ")
rs = s[::-1]
if(s == rs):
    print("String is a palindrome")
else:
    print("String is not a palindrome")

# This program got executed successfully and the output has been verified.
