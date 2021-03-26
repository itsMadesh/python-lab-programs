import math


def cosXseries(x, n):
    radian = math.radians(x)
    sum = 1
    fact = 1
    sign = 1
    power = 1
    for i in range(1, n):
        sign, power = -sign, power*2
        sum += sign*(pow(radian, power)/math.factorial(power))
    return sum


x = int(input("Enter the degree in x:"))
n = int(input("How many terms do you want to sum:"))
print("cos",x,"degree=",round(cosXseries(x, n), 2))
