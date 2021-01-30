# 38. Write a program to find maximum occurring character in a string.

s = input("Enter a string : ")
moc, ch = 0, ""
for c in s:
    if moc < s.count(c):
        moc = s.count(c)
        ch = c
print("maximum occurring character : ", ch)

# This program got executed successfully and the output has been verified.
