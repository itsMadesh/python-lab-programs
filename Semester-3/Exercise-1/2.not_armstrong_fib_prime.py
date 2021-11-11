# 2. If the given input is not an Armstrong number, then find the closest higher order
# Armstrong number and perform the above given task.

def is_arms(n, count):
    sum = 0
    while(n > 0):
        rem = n % 10
        sum += rem**count
        n = n//10
    return sum


def is_prime(s):
    if(s == 0 or s == 1):
        return 0
    for i in range(2, int(s/2)+1, 1):
        if(s % i == 0):
            return 0
    else:
        return 1


def get_fib_and_prime_list(n):
    fibo_list = []
    prime_list = []
    s = 0
    a = -1
    b = 1
    while(a+b <= n):
        s = a+b
        a = b
        b = s
        fibo_list.append(s)
        if(1 == is_prime(s)):
            prime_list.append(s)
    print("Fibonacci series:")
    print(fibo_list)
    print("The alternative prime numbers are:")
    print([prime_list[i]
           for i in range(len(prime_list)) if i % 2 == 0])


n = int(input("Enter a number:"))
if(n != is_arms(n, len(str(n)))):
    print("Given number is not armstrong number")
    print("Finding closest armstrong number of the given number")
    i = n-1
    j = n+1
    while(True):
        if(i == is_arms(i, len(str(i)))):
            print(i, "is the closest armstrong number")
            get_fib_and_prime_list(i)
            break
        elif(j == is_arms(j, len(str(j)))):
            print(j, "is the closest armstrong number")
            get_fib_and_prime_list(j)
            break
        i -= 1
        j += 1
else:
    print(n, "is armstrong number")
    get_fib_and_prime_list(n)
