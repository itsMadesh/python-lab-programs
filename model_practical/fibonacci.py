#Write a program to generate Fibonacci numbers within the given limit.
m=int(input("Enter a starting limit:"))
n = int(input("Enter a number of terms :"))

s=0
a=1
b=0
fib=[]
while(s<=n):
    fib.append(s)
    s=a+b
    a=b
    b=s
print(fib[m:]) 
    




