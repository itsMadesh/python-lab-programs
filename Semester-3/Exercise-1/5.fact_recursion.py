# 5. Write a recursive function to find the factorial of a number

def fact(n):
    if(n<2):
        return 1
    return n*fact(n-1) 
n=int(input("Enter a number:"))
print(str(n)+"!=",fact(n))   