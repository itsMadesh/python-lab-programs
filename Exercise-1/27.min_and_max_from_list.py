# 27. Write a program to find the maximum and minimum element in an list .

n = int(input("Enter size of list : "))
arr = []
for i in range(n):
    arr.append(int(input("Enter element :")))
print("Minimum in list : ", min(arr))
print("Maximum in list : ", max(arr))

# This program got executed successfully and the output has been verified.
