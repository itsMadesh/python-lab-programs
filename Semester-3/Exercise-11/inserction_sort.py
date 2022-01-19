def inserction_sort(a, n):
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


a = []
n = int(input("Enter size of the array:"))
for i in range(n):
    a.append(input("Enter a value:"))
print("Sorted list:", inserction_sort(a, n))
