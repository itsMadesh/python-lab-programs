def fact(n):
    if n <= 1:
        return 1
    return n*fact(n-1)

n = int(input("Enter a factorial number:"))
print("factorial of", n,"is",fact(n))
