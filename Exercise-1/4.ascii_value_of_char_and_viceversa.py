# 4. WAP to display the ASCII value of a char got as input from the user and vice versa.

char = input("Enter a character :")
ascii_value = ord(char)
print("Ascii value of", char, "is", ascii_value)
ascii_value = int(input("Enter a ascii value :"))
char = chr(ascii_value)
print("character of ", ascii_value, "is", char)

# This program got executed successfully and the output has been verified.
