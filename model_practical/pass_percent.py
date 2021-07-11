
#1.Given a file containing students mark list write a program to print pass percentage. 
#Hint: passpercentage=(no of students passed / no. of students attended *100)
attended=0
passed=0
fp=open("model_practical//mark_list.txt","r")
for student in fp.readlines():
    marks=student.split()
    attended+=1
    check=int(marks[1])//5
    if(check>=35):
        passed+=1
        
print("Number of students passed:",passed)
print("Number of students attented:",attended)        
pass_percentage=(passed/attended)*100 
print("pass percentage:",pass_percentage)

