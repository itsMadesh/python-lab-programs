
def find(arr, search):
    for a in arr:
        if(a==search):
           return "found"
    return  "not present"

arr = [1,3,4,5]
search=6
print(find(arr,search))


 


