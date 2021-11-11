# 4. Write a recursive function to check whether the given string is a Palindrome or not. 
def palindrome(str,front,back):
    if(len(str)//2==front):
        return 1
    if(str[front]!=str[back]):
        return 0
    return palindrome(str,front+1,back-1)         
str=input("Enter a string:")
n=len(str)-1
if(1==palindrome(str,0,n)):
    print("'{}' is palindrome".format(str))
else:
    print("'{}' is not palindrome".format(str))


