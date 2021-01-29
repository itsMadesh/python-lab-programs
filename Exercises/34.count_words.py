# 34. Write a program to count the total number of words in a string.

s = input("Enter a string : ")
w, f = 0, True
for c in s:
    if(c != ' ' and f):
        w = w+1
        f = False
    elif (c == ' '):
        f = True
print("Count of words is : ", w)

# This program got executed successfully and the output has been verified.
