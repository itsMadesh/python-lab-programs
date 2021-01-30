# 20. Write a program to read n number of values in an list and display it in reverse order.

n = int(input("How many elements do you want to include into list :"))
list_1 = []
print("Enter any", n, "list elements :")
for i in range(0, n, 1):
    a = int(input())
    list_1.append(a)
print("Original list is", list_1)
i = -1
reverse_order = []
while(i >= -n):
    a = list_1[i]
    reverse_order.append(a)
    i = i+-1
print(reverse_order)

# This program got executed successfully and the output has been verified.
