# 1. Get an input from the user and check if that input is an Armstrong number. If yes,
# print the Fibonacci series of the input. Identify all the prime numbers in the generated
# Fibonacci list and print only the alternate prime numbers.
def get_digit_count(n):
    count = 0
    while(n > 0):
        n = n//10
        count += 1
    return count


def is_arms_num(n, count):
    sum = 0
    while(n > 0):
        rem = n % 10
        sum += rem**count
        n = n//10
    return sum


def is_prime_num(s):
    if(s == 0 or s == 1):
        return 0
    for i in range(2, int(s/2)+1, 1):
        if(s % i == 0):
            return 0
    else:
        return 1


def get_fib_and_prime_list(n):
    fibo_list, prime_list = [], []
    s = 0
    a = -1
    b = 1
    while(a+b <= n):
        s = a+b
        a = b
        b = s
        fibo_list.append(s)
        if(1 == is_prime_num(s)):
            prime_list.append(s)
    return fibo_list, prime_list


n = int(input("Enter a number:"))
count = get_digit_count(n)
if(n == is_arms_num(n, count)):
    fibo_list, prime_list = get_fib_and_prime_list(n)
    print("Fibonacci series:")
    print(fibo_list)
    print("The alternative prime numbers are:")
    print([prime_list[i]
           for i in range(len(prime_list)) if i % 2 == 0])
else:
    print(n, "is not armstrong number")
