# 49. Write a function with a parameter n that returns the nth Fibonacci number. The function must be recursive.

n = int(input("Enter a number : "))


def fib(n):
    if n <= 1:
        return n
    return fib(n-1)+fib(n-2)


print("fib : ", fib(n))

# This program got executed successfully and the output has been verified.
