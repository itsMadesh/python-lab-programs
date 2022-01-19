def linear_search(arr,key):
    for i in range(len(arr)):
        if(arr[i]==key):
            print("\nElement found at index-"+str(i))
            return
    print("\nElement not found in array")
arr=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    arr.append(int(input("\nEnter value:")))
key=int(input("\nEnter element which you want search from the given array:"))
linear_search(arr,key)
