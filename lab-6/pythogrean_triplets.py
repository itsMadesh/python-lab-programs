import math


def pythagorean_triplets(n):
    for a in range(1, n):
        for b in range(1, a):
            c = math.sqrt(a*a+b*b)
            if c % 1 == 0:
                print((a, b, int(c)))

n=int(input("Enter-n:"))
pythagorean_triplets(n)
