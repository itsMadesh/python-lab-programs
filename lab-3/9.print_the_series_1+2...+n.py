n = int(input("Enter a limit :"))
t = ""
sum = 0
for i in range(1, n+1):
    t += (" + " if i != 1 else "") + str(i)
    sum += i
print(t, "=", sum)
