def newton_method(num,l=100):
    a=float(num)
    for i in range(l):
        num=0.5*(num+(a/num))
    return num
a=int(input("Enter a number :"))
print("Square root of", a," is", newton_method(a))       