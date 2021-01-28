n = abs(int(input("Enter a integer :")))
r = 0
while(n != 0):
    r = n % 10+r
    n = n//10
print(r)
