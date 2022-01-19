def shell_sort(a,n):
    interval=n//2
    while(interval>0):
        for i in range(interval,n):
            tempvalue=a[i]
            j=i
            while(j>=interval and a[j-interval]>tempvalue):
                a[j]=a[j-interval]
                j-=interval
            a[j]=tempvalue
        interval//=2
a=[]
n=int(input("Enter size of the array:"))
for i in range(n):
    a.append(input("Enter a value:"))
shell_sort(a,n)
print("Sorted array:",a)

