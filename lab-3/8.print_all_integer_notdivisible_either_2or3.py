n = int(input("Enter a limit :"))
for i in range(1, n+1):
    if(i % 2 != 0 and i % 3 != 0):
        print("Not divisible either 2 or 3 is", i)
