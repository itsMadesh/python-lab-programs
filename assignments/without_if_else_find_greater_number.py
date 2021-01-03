# This program will find largest among three numbers without if_else
largest = int(input("Enter number-1 :"))
for i in range(2, 4):
    a = int(input("Enter number-{0} :".format(i)))
    if (a >= largest):
        largest = a
print("largest among 3 numbers is", largest)
