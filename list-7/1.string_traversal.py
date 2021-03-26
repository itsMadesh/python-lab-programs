a=input("Enter sentence/word:")
print("Normal string traversal:")
for i in range(len(a)):
    print(a[i],end=" ")
print("\nReverse string traversal:")    
for i in range(len(a)-1,-1,-1):
    print(a[i],end=" ")