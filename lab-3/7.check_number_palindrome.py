n = int(input("Enter a number :"))
s = n
num = 0
while(n > 0):
    r = n % 10
    num = num*10+r
    n = n//10
if(s == num):
    print("Given number is palindrome")
else:
    print("Given number is not palindrome")
