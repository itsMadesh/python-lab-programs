# 28. Write a program to sort elements of list in ascending order.

n = int(input("Enter size of list : "))
arr = []
for i in range(n):
    arr.append(int(input("Enter element :")))
arr.sort()
print("Sorted list : ", arr)

# This program got executed successfully and the output has been verified.
