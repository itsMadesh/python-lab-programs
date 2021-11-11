#2. Temperature conversion

class Temp:
	def farenheit(self,c):
		self.f=(c*1.8)+32
		print("Farenheit is",self.f)
	def celcius(self,f):
		self.c=(f-32)*(5/9)
		print("Celcius is",self.c)		
while(1):
	cal=Temp()
	print("Conversion operations\n1.Convert Celcius to farenheit\n2.Convert farenheit to celcius\n3.Exit")
	choice=int(input("Enter your choice(1/2/3):"))
	if(choice==3):
		break
	if(choice==1):
		c=int(input("Enter celcius value:"))
		cal.farenheit(c)
	elif(choice==2):
		f=int(input("Enter Farenheit value:"))
		cal.celcius(f)
	else:
		print("Invalid Input")	