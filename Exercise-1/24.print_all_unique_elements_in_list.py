# 24. Write a program to print all unique elements in an list.

num = []
n = int(input("How many elements do you want to inclued into list:"))
print("Enter a list elements :")
for i in range(0, n):
    a = int(input())
    num.append(a)
print("Given list is ",num)
unique_elements = []
for i in range(0, n):
    if(num[i] not in unique_elements):
        unique_elements.append(num[i])
print("Unique elements in list :",unique_elements)

# This program got executed successfully and the output has been verified.
