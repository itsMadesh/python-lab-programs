n = int(input("Enter a number :"))
odd=0
even=0
for i in range(2,n):
    if(i%2==0):
        even+=i
    else:
        odd+=i
print("Sum of the odd numbers betweem 1 to",n,":",odd)   
print("Sum of the even numbers betweem 1 to",n,":",even)       