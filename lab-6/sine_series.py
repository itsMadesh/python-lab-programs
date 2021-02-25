import math


def sineXseries(x, n):
    radian = math.radians(x)
    sum = 0
    power = 1
    sign = 1
    for i in range(0, n):
        sum = sum+sign*(radian**power/math.factorial(power))
        sign = -sign
        power += 2
    return sum


x = int(input("Enter a degree in x:"))
n = int(input("How many terms do you want to sum:"))
print(round(sineXseries(x, n), 2))
