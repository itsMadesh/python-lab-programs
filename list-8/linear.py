def linear_search(a,b):
    for i in range(n-1):
        if(b==a[i]):
            print("Number",b,"found in index-",i)
            break
    else:
        print("Number not found in list-a")        
a=[]
n=int(input("Enter no.of inputs:"))
for i in range(n):
    x=int(input("Enter a value in index-"+str(i)+":"))
    a.append(x)
b=int(input("Enter number to be searched:"))   
linear_search(a,b) 
  