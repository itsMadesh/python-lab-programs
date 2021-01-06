a = int(input("Enter a starting range :"))
b = int(input("Enter a ending range :"))
for i in range(max(a, 2), b+1):
    for j in range(2, i):
        if(i % j == 0):
            break
    else:
        print(i)
