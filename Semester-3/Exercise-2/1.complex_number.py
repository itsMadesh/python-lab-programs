#1.COMPLEX NUMBER

class Complex:
	def add(self,r1,i1,r2,i2):
		self.r3=r1+r2
		self.i3=i1+i2
		print("Z1+Z2=",self.r3,"+i",self.i3)
	def sub(self,r1,i1,r2,i2):
		self.r3=r1-r2
		self.i3=i1-i2
		print("Z1-Z2=",self.r3,"+i",self.i3)
	def multiply(self,r1,i1,r2,i2):
		self.r3=(r1*r2)-(i1*i2)
		self.i3=(r1*i2+i1*r2)
		print("Z1*Z2=",self.r3,"+i",self.i3)
	def division(self,r1,i1,r2,i2):
		self.r3=((r1*r2)-(i1*(-i2)))/(r2*r2+i2*i2)
		self.i3=(r1*(-i2)+i1*r2)/(r2*r2+i2*i2)
		print("Z1/Z2=",self.r3,"+i",self.i3)
num=Complex()
while(1):
	print("Operations:\n1.Add\n2.Sub\n3.Multiply\n4.Division\n5.Exit")
	choice=int(input("Enter Your choice(1/2/3/4/5):"))
	if choice==5:
		break
	r1=int(input("Enter real number for z1:"))
	i1=int(input("Enter img number for z1:"))
	r2=int(input("Enter real number for z2:"))
	i2=int(input("Enter img number for z2:"))
	if choice==1:
		num.add(r1,i1,r2,i2)
	elif choice==2:
		num.sub(r1,i1,r2,i2)
	elif choice==3:
		num.multiply(r1,i1,r2,i2)
	elif choice==4:
		num.division(r1,i1,r2,i2)
	else:
		print("Invalid Input")	