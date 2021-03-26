def selectionsort(a):
    for i in range(n):
        min1=i
        for j in range(i+1,n):
            if(a[min1]>a[j]):
                min1=j
        a[i],a[min1]=a[min1],a[i]
    print("sorted array:",a)

a = []
n = int(input("How many elements does you want to include into your list:"))
for i in range(n):
    b = input("Enter element-"+str(i+1)+":")
    a.append(int(b))
print("Unsorted array:",a)
selectionsort(a)