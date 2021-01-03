# This program will reverse entered number
n = abs(int(input("Enter a number:")))
num = 0
while(n > 0):
    r = n % 10
    num = num*10+r
    n = (n//10)
print("reverse of given number : ", num)
