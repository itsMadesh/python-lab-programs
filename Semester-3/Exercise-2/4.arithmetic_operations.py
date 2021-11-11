#4. Arithmetic operation

class Arithmetic:
	def operations(self,a,b):
		self.result=a+b
		print(a,"+",b,"=",self.result)
		self.result=a-b
		print(a,"-",b,"=",self.result)
		self.result=a*b
		print(a,"*",b,"=",self.result)
		self.result=a/b
		print(a,"/",b,"=",self.result)
		self.result=a%b
		print(a,"%",b,"=",self.result)
		self.result=a//b
		print(a,"//",b,"=",self.result)
		self.result=a**b
		print(a,"**",b,"=",self.result)
obj=Arithmetic()
while(1):
	print("1.perform operations\n2.Exit")
	choice=int(input("Enter your choice(1/2):"))
	if choice==1:
		print("Enter a and b value to perform arithmetic operations:")
		a=int(input("a="))
		b=int(input("b="))
		obj.operations(a,b)
	elif choice==2:
		break
	else:
		print("Invalid input")	