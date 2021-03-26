a=input("Enter a string:")
b=""
for i in range(len(a)-1,-1,-1):
    b+=a[i]
if(a==b):
    print("Given string is palindrome") 
else:
    print("Given string is not palindrome")       
    