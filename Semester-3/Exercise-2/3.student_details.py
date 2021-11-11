#3. Student details

class Student:
	def details(self):
		self.name=input("\nEnter Student name:")
		self.roll=int(input("\nEnter Roll.no:"))
		self.college_name=input("\nEnter college name:")
		self.year=int(input("\nEnter Studying which year:"))
		self.age=int(input("\nEnter student age:"))
		self.dept=input("\nEnter student belongs to which department:")
n=int(input("Enter number of students:"))
students_details=[]
for i in range(n):
	student=Student()
	student.details()
	students_details.append(student)
print("\nStudents Details:")	
for i in students_details:
	print("[Name:%s,Roll.no:%d,college name:%s,Year:%d,Age:%d,Dept:%s]"%(i.name,i.roll,i.college_name,i.year,i.age,i.dept))