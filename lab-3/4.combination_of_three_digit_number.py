n = (input("Enter a number :"))
s = int(n)
if(s < 100 and s > 999):
    print(" Invalid input ")
else:
    for i in range(3):
        for j in range(3):
            if(i == j):
                continue
            for k in range(3):
                if(i != k and j != k):
                    print(n[i]+n[j]+n[k])
