a = int(input("Enter a first number:"))
b = int(input("Enter a second number:"))


def max(a, b):
    return a if a > b else b


print("maximum of two numbers is ", max(a, b))
