# 25. Write a program to merge two lists of same size sorted in decending order.

list_1 = []
list_2 = []
n = int(input("How many elements do you want to inclued into list:"))
print("Enter a list-1 elements :")
for i in range(0, n):
    a = int(input())
    list_1.append(a)
print("list-1 is ", list_1)
print("Enter a list-2 elements :")
for i in range(0, n):
    a = int(input())
    list_2.append(a)
print("list-2 is ", list_2)
merge_list = list_1+list_2
print("Merged list:",merge_list)
merge_list.sort(reverse=True)
print("Merged list in descending order :",merge_list)

# This program got executed successfully and the output has been verified.
