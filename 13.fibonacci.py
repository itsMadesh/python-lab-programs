n = int(input("Enter a number of terms :"))
if(n < 1):
    print("invalid input")
s = 0
a = 0
b = 1
arr = []
if(n >= 1):
    print(0, end=" ")
if(n >= 2):
    print(1, end=" ")
for i in range(2, n):
    s = a+b
    print(s, end=" ")
    a = b
    b = s
