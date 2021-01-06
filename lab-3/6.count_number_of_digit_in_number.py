n = abs(int(input("Enter a number :")))
i = 0
while(n > 0):
    n = n//10
    i = i+1
print("Number of digits is ", i)
