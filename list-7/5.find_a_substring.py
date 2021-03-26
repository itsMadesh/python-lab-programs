a=input("Enter a string:")
b=input("Enter a substring:")
def substr(a,b):
    return a.find(b)
if (substr(a,b)==-1):
    print("Does not contain given substring")
else:
    print("Substring is found in index-",substr(a,b))    