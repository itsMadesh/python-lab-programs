# 43. Write the function int countchars(char string[], int ch) which returns the number of times the character
# ch appears in the string.

s = input("Enter a string : ")
ch = input("Enter a character : ")


def count_chars(s, ch):
    count = 0
    for c in s:
        if c == ch:
            count += 1
    return count


print("No of ", ch, " in string : ", count_chars(s, ch))

# This program got executed successfully and the output has been verified.
