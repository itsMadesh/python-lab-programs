# 26. Write a program to count the frequency of each element of an list.

n = int(input("How many elements do you want to include into list :"))
arr = []
print("Enter any", n, "list elements :")
for i in range(0, n):
    a = int(input())
    arr.append(a)
print("List is ", arr)
unique_arr = list(set(arr))
for i in range(0, len(unique_arr)):
    print("Frequency of element",
          unique_arr[i], " is", arr.count(unique_arr[i]))

# This program got executed successfully and the output has been verified.
