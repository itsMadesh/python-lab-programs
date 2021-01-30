# 29. Write a program to sort elements of the list in descending order .

n = int(input("Enter size of list : "))
arr = []
for i in range(n):
    arr.append(int(input("Enter element :")))
arr.sort(reverse=True)
print("Sorted list in decending order : ", arr)

# This program got executed successfully and the output has been verified.
