# 42. Write a function generateprimes(int limit) to generate all the prime numbers between 2 and some given
# limit and return them as an array. Print all elements from array.

n = int(input("Enter a limit : "))


def generate_primes(n):
    primes = []
    for i in range(2, n+1):
        for j in range(2, i):
            if(i % j == 0):
                break
        else:
            primes.append(i)
    return primes


print("primes within given limit : ", generate_primes(n))

# This program got executed successfully and the output has been verified.
