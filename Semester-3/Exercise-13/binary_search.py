def binary_search(arr,l,r,key):
    if(l>=r):
        print("Element not found in array")
        return
    mid=l+(r-l)//2
    if(arr[mid]==key):
        print("Element found at index-"+str(mid))
    elif(arr[mid]>key):
        binary_search(arr,l,mid-1,key)
    else:
        binary_search(arr,mid+1,r,key)
arr=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    arr.append(int(input("Enter value:")))
arr.sort()
print(arr)
key=int(input("Enter element which you want search from the given array:"))
binary_search(arr,0,n-1,key)