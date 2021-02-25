def power(base, exp):
    if (exp == 0):
        return 1
    elif (int(exp % 2) == 0):
        return (power(base, int(exp / 2)) *
                power(base, int(exp / 2)))
    else:
        return (base * power(base, int(exp / 2)) *
                power(base, int(exp / 2)))


base = int(input("Enter a base value:"))
exp = int(input("Enter a exponent value:"))
print(base, "power", exp, "is", power(base, exp))
