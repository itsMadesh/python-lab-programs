# 14. Write a Program to check whether an alphabet is a vowel or consonant.

char = input("Enter a alphabet :")
if not char.isalpha():
    print("Invalid input")
elif char in ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'):
    print(char, "is a vowel")
else:
    print(char, "is a consonant")

# This program got executed successfully and the output has been verified.
