# 11. Write a Program to read roll no, name and marks of three subjects and calculate the total, percentage and grade.

roll_no = input("Enter a roll_no of the student :")
name = input("Enter a name of the student :")
sub1_mark = int(input("Enter a mark of the subject-1 :"))
sub2_mark = int(input("Enter a mark of the subject-2 :"))
sub3_mark = int(input("Enter a mark of the subject-3 :"))
total_mark = sub1_mark+sub2_mark+sub3_mark
print("Total mark is", total_mark)
percentage = total_mark/3
print("Percentage is", percentage)
if(percentage > 80 and percentage <= 100):
    print("Grade is A")
elif(percentage > 60 and percentage <= 80):
    print("Grade is B")
elif(percentage >= 35 and percentage <= 60):
    print("Grade is c")
else:
    print("fail")

# This program got executed successfully and the output has been verified.
