def heapify(arr,i,n):
    j=i
    l=2*i+1
    r=2*i+2
    if(l<n and arr[j]<arr[l]):
        j=l
    if(r<n and arr[j]<arr[r]):
        j=r
    if(i!=j):
        arr[i],arr[j]=arr[j],arr[i]
        heapify(arr,j,n)
def heapsort(arr):
    n=len(arr)
    for i in range(n//2-1,-1,-1):
        heapify(arr,i,n)
    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heapify(arr,0,i)
    print("Sorted array:",arr)

arr=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    arr.append(int(input("Enter value:")))
heapsort(arr)
