# 44. Write the function replace(char string[], char from[], char to[]) which finds the string 'from' in the
# string 'string' and replaces it with the string 'to'.

s = input("Enter a string : ")
f = input("Enter a from string : ")
t = input("Enter a to string : ")


def replace(s, f, t):
    return s.replace(f, t)


print("answer string : ", replace(s, f, t))

# This program got executed successfully and the output has been verified.
