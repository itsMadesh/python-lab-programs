# This program will add digits of entered number
n = abs(int(input("Enter a number:")))
sum = 0
while(n > 0):
    r = n % 10
    sum = sum+r
    n = int(n/10)
print("sum of digits is ", sum)
