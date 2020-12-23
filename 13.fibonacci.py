n = int(input("Enter a number of terms :"))
if(n < 1):
    print("invalid input")
s = 0
a = -1
b = 1
for i in range(0, n):
    s = a+b
    print(s, end=" ")
    a = b
    b = s
