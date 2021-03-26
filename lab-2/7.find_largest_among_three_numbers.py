a = int(input("Enter a first number :"))
b = int(input("Enter a second  number :"))
c = int(input("Enter a third number :"))
if(a > b and a > c):
    print(a,"is the maximum of 3 numbers")
elif(b > a and b > c):
    print(b,"is the maximum of 3 numbers")
else:
    print(c,"is the maximum of 3 numbers")
