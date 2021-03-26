'''1. Try using string built-in functions like isalnum(), 
isalpha(),isdigit(),islower(),isupper(),find(str,beg,end),index(str,beg,end)....'''

string=input("Enter a string:")
print("Given string is ","lower" if string.islower() else "not lower")
print("Given string is ","upper" if string.isupper() else "not upper")
print("Given String is ","contains alpha or numeric" if string.isalnum() else "not contains alpha or numeric")
print("Given string is ","conatins only alphabets" if string.isalpha() else "not contains only alphabets")
print("Given string is ","contains only digits" if string.isdigit() else "not contains only digits")
substr=input("Enter  a substring:")
print( "Substring is found in index-:",string.find(substr) if string.find(substr)!=-1 else "Substring is not in given given string")
