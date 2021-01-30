# 37. Write a program to count total number of vowel or consonant in a string.

s = input("Enter a string : ")
vc, cc = 0, 0
for c in s:
    if c in ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'):
        vc += 1
    else:
        cc += 1
print("No of vowels : ", vc)
print("No of consonant : ", cc)

# This program got executed successfully and the output has been verified.
