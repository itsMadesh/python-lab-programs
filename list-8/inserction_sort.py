# inserction sort:
def inserction_sort(a):
    for i in range(1, len(a)):
        value = a[i]
        j = i-1
        while(j >= 0 and value < a[j]):
            a[j+1] = a[j]
            j -= 1
        a[j+1] = value
    return a


a = []
n = int(input("How a many elements do you want to include into your list:"))
for i in range(n):
    b = input("Enter element-"+str(i+1)+":")
    a.append(int(b))
print("Unsorted list:",a)
print("sorted list:",inserction_sort(a))
