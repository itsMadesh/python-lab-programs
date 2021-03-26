# 2. Modify the contents of the nested dictionary
c = 'y'
while(c == 'y'):
    print("MENU\n1.Print a nested dictionary\n2.Add a another dictionary\n3.Delete elements from a nested dictionary \n4.Delete a dictionary from a nested dictionary \n5.Iterating through the dictionary")
    ch = int(input("Enter your choice(1/2/3/4/5):"))
    students={"Madesh":{"Age": 18,"Branch": "IT", "Sec": "S2", "Roll.no": "S02031"},"Dravid":{"Age": 18,"Branch": "IT", "Sec": "S2", "Roll.no": "S02017"}}
    if(ch==1):
        print("Nested dictionary:",students)
    elif(ch==2):
        students["Antony"]={"Age": 18,"Branch": "IT", "Sec": "S2", "Roll.no": "S02011"}
        print("Add a another dictionary:",students)
    elif(ch==3):
        del students["Madesh"]["Age"]
        print("After delete element from a dictionary:",students)
    elif(ch==4):
        del students["Dravid"]   
        print("After Delete a dictionary from a nested dictionary:",students)  
    elif(ch==5):
        for k,v in students.items():
            print(k,":",v)
    else:
        print("INVALID CHOICE")        
    c=input("Do you want to continue(y/n):") 


'''l = {1: "a", 2: "b"}
for k, v in l.items():
    print(k, v)

print({input("enter key : "): input("enter value : ") for i in range(3)} for j in range(3) )'''
