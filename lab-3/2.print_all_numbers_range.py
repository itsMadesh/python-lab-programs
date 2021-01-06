n = int(input("Enter a divide number :"))
a = int(input("Enter a starting range :"))
b = int(input("Enter a ending range :"))
for i in range(a, b+1):
    if(i % n == 0):
        print("Divisible number", i)
