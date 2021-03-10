def binarysearch(a, l, r, search_key):
    while(l <= r):
        mid = l+(r-l)//2
        if(a[mid] == search_key):
            print("Given value find in a index:", mid)
            break
        elif(a[mid] < search_key):
            l = mid+1
        else:
            r = mid-1
    print("Element not found in list-a")


a = []
n = int(input("how a many elements do you want to include into your list:"))
for i in range(n):
    b = input("Enter element-"+str(i+1)+":")
    a.append(int(b))
a.sort()
print(a)
search_key = int(input("Enter a search value:"))
binarysearch(a, 0, n-1, search_key)
