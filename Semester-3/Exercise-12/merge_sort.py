def mergearr(arr,l,r,mid):
    arr1=arr[l:mid+1]
    arr2=arr[mid+1:r+1]
    i=j=0
    k=l
    m=len(arr1)
    n=len(arr2)
    while(i<m and j<n):
        if(arr1[i]<arr2[j]):
            arr[k]=arr1[i]
            i+=1
        elif(arr1[i]>=arr2[j]):
            arr[k]=arr2[j]
            j+=1
        k+=1
    while(i<m):
        arr[k]=arr1[i]
        i+=1
        k+=1
    while(j<n):
        arr[k]=arr2[j]
        j+=1
        k+=1
def mergesort(arr,l,r):
    if(l<r):
        mid=l+(r-l)//2
        mergesort(arr,l,mid)
        mergesort(arr,mid+1,r)
        mergearr(arr,l,r,mid)
arr=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    arr.append(int(input("Enter value:")))
mergesort(arr,0,len(arr)-1)
print("Sorted array:",arr)



