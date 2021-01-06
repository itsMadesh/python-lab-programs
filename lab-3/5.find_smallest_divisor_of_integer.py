n = int(input("Enter a integer :"))
for i in range(2, n+1):
    if(n % i == 0):
        print("Smallest divisor is", i)
        break
