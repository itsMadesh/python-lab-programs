# PYTHON STRING METHODS

# capitalize()
print("Method: capitalize() ")
a = input("Enter a string :")
print("Converts first character to uppercase :", a.capitalize())

# casefold()
print("Method: casefold() ")
a = input("Enter a string :")
print("converts string into lowercase :", a.casefold())

# center()
print("Method: center() ")
a = input("Enter a string :")
print("Returns a centered string :", a.center(20))

# count()
print("Method: count() ")
a = input("Enter a string :")
value = input("Enter a counting char in a given str :")
print("count the specified value occur in a string:", a.count(value))

# encode()
print("Method: encode() ")
a = input("Enter a string :")
print("different Encoding strings are:")
print(a.encode(encoding="ascii", errors="backslashreplace"))
print(a.encode(encoding="ascii", errors="ignore"))
print(a.encode(encoding="ascii", errors="strict"))
print(a.encode(encoding="ascii", errors="namereplace"))
print(a.encode(encoding="ascii", errors="replace"))
print(a.encode(encoding="ascii", errors="xmlcharrefreplace"))

# endswith()
print("Method: endswith() ")
a = input("Enter a string :")
check = input("Enter a value for checking endswith :")
print(a.endswith(check))

# expandtabs()
print("Method: expandtabs() ")
a = input("Enter a string:")
value = int(input("How many tabs do you want to expand:"))
print("Expand tabs for a given string:", a.expandtabs(value))

# find()
print("Method: find() ")
a = input("Enter a string :")
value = input("Enter finding word:")
print("position of a", value, " in a given string", a.find(value))

# format()
print("Method: format() ")
a = input("Enter a string :")
print(a.format(10, 20, 30))

# index()
print("Method: index() ")
a = input("Enter a string :")
value = input("Enter a value for find its position in a given string :")
print(a.index(value))

# isalnum()
print("Method: isalnum() ")
a = input("Enter a string :")
print("returns True if all the characters are alpha or numeric, otherwise False :", a.isalnum())

# isalpha()
print("Method: isalpha() ")
a = input("Enter a string :")
print("returns True if all the characters are alphabets, otherwise False :", a.isalpha())

# isdecimal()
print("Method: isdecimal() ")
a = input("Enter a string :")
print("returns True if all the characters are decimal, otherwise False :", a.isdecimal())

# isdigit()
print("Method: isdigit() ")
a = input("Enter a string :")
print("returns True if all the characters are digits, otherwise False:", a.isdigit())

# isidentifier()
print("Method : isidentifier() ")
a = input("Enter a string :")
print("returns True if all the characters is a valid identifier, otherwise False :", a.isidentifier())


# islower()
print("Method : islower() ")
a = input("Enter a string :")
print("returns True if all the characters are in lower_case, and numbers,symbols,spaces are not checked, otherwise False:", a.islower())

# isnumeric()
print("Method : isnumeric() ")
a = input("Enter a string :")
print("Returns True if all characters in the string are numeric, otherwise False :", a.isnumeric())


# isprintable()
print("Method : isprintable() ")
a = input("Enter a string :")
print("Returns True if all characters in the string are printable, otherwise False :", a.isprintable())

# isspace()
print("Method : isspace() ")
a = input("Enter a string :")
print("Returns True if all characters in the string are whitespaces, otherwise False :", a.isspace())

# isupper()
print("Method : isupper() ")
a = input("Enter a string :")
print("Returns True if all characters are in upper_case, otherwise False :", a.isupper())

# istitle()
print("Method : istitle() ")
a = input("Enter a string :")
print("Returns True if the string follows the rules of a title, otherwise False :", a.istitle())

# join()
print("Method : join() ")
a = input("Enter a string :")
print("Joins the elements of an iterable to the end of the string :", "1".join(a))

# ljust()
print("Method : ljust() ")
a = "White"
b = a.ljust(20)
print("Returns a left justified version of the string:", b+'house')

# lower()
print("Method : lower() ")
a = input("Enter a string :")
print("Converts a string into lower case :", a.lower())

# lstrip()
print("Method : lstrip() ")
a = input("Enter a string :")
print("Returns a left trim version of the string:", a.lstrip(" "))

# maketrans() and translate()
print("Methods : maketrans() and translate()")
a = " madesh"
x = "seh"
y = "dyy"
mytable = a.maketrans(x, y)
print(a.translate(mytable))

# partition()
print("Method : partition() ")
a = "He walks on road"
print("Returns a tuple where the string is parted into three parts:", a.partition("on"))

# replace()
print("Method : replace() ")
a = "I like chocolates"
x = "chocolates"
y = "you"
print("Returns a string where a specified value is replaced with a specified value:", a.replace(x, y))

# rfind()
print("Method : rfind() ")
a = input("Enter a string :")
b = input("Enter a findind value:")
print("Searches the string for a specified value and returns the last position of where it was found:", a.rfind(b))

# rindex()
print("Method : rindex() ")
a = input("Enter a string :")
b = input("Enter a findind value:")
print("Searches the string for a specified value and returns the last position of where it was found:", a.rindex(b))

# rjust()
print("Method : rjust() ")
a = "White"
b = a.rjust(20)
print("Returns a right justified version of the string:", b+'house')

# rpartition()
print("Method : rpartition() ")
a = "He walks on road"
print("Returns a tuple where the string is parted into three parts:", a.rpartition("on"))

# rsplit()
print("Method : rsplit() ")
a = input("Enter a string :")
print("Splits the string at the specified separator, and returns a list:",
      a.rsplit(" ", 2))

# rstrip()
print("Method : rstrip() ")
a = input("Enter a string :")
print("Returns a right trim version of the string:", a.rstrip(","))


# split()
print("Method :split() ")
a = input("Enter a string :")
print("Splits the string at the specified separator, and returns a list:", a.split(" "))

# splitlines()
print("Method : splitlines() ")
a = "bike\ncar\naeroplane"
print("Splits the string at line breaks and returns a list:", a.splitlines())

# startswith()
print("Method : startswith() ")
a = "bike car aeroplane"
print("Returns true if the string starts with the specified value:", a.startswith("b"))

# strip()
print("Method : strip() ")
a = input("Enter a string :")
print("Returns a trimmed version of the string:", a.strip(" "))


# swapcase()
print("Method : swapcase() ")
a = input("Enter a string :")
print("Swaps cases, lower case becomes upper case and vice versa:", a.swapcase())

# title()
print("Method : title() ")
a = input("Enter a string :")
print("Converts the first character of each word to upper case:", a.title())

# upper()
print("Method : upper() ")
a = input("Enter a string :")
print("Converts a string into upper case:", a.upper())

# zfill()
print("Method : zfill() ")
a = input("Enter a string :")
print("Fills the string with a specified number of 0 values at the beginning:", a.zfill(10))
