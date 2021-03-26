a=(1,2,3,4,5,)
b=(6,7,8,9,10)
print("Tuple-a is:",a)
print("Tuple-b is:",b)
#length
print("length of tuple-a is:",len(a))
#memebership
i=10
if i in a:
    print("True")    
#concatenation    
print("concatenate tuple a and b is:",a+b)   
#repitition
print("repitition:",a*2,b*2)
#iteration
print("Iterate elements in tuple-a:")
for i in a:
    print(i,end=" ")