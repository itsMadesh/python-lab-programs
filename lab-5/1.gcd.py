a = int(input("Enter a number a :"))
b = int(input("Enter a number b :"))
for i in range(2, min(a, b)+1):
    if(a % i == 0 and b % i == 0):
            gcd = i
print("Gcd of", a,"and", b," is", gcd)
