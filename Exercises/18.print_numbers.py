# 18. (a).This program will prints all odd numbers between 10 and 60.
print("odd numbers between 10 and 60 are ", end="")
for i in range(10, 61):
    if(i % 2 != 0):
        print(i, end=" ")

# (b).This program will prints all the numbers between 1 and 50,with 10 numbers on each line with all the columns aligned with proper spaces.
print("\nAll the numbers between 1 and 50 are ")
for i in range(1, 51):
    if i % 10 == 0:
        print(i, end="\n")
    else:
        if(i < 10):
            print('0'+str(i), end=" ")
        else:
            print(i, end=" ")


# (c).This program will get a number from user and prints the number muliplied by 10.Repeat until 0 is entered.
n = 1
while(True):
    n = int(input("Enter a number :"))
    if n == 0:
        break
    print(n, "is multiplied by 10 :", n*10)
