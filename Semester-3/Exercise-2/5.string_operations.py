#5. string operations

class String:
	def upper_(self,str):
		print("Result:",str.upper())
	def lower_(self,str):
		print("Result:",str.lower())
	def capitalize_(self,str):
		print("Result:",str.capitalize())
	def count_(self,str):
		c=input("Enter a char or word to get no.of times it appears in the given string:")
		print("Result:",str.count(c,0,len(str)))	
	def find_(self,str):
		search=input("Enter a char or word to find its position in the given string:")
		print("Result:",str.find(search,0,len(str)))
while(1):
	print("String operations:")
	print("1.Upper()\n2.Lower()\n3.Capitalize()\n4.Count()\n5.Find()\n6.Exit")
	c=int(input("Enter a choice(1/2/3/4/5/6):"))
	if(c==6):
		break
	str=input("Enter a string:")
	obj=String()	
	if(c==1):
		obj.upper_(str)
	elif(c==2):
		obj.lower_(str)
	elif(c==3):
		obj.capitalize_(str)
	elif(c==4):
		obj.count_(str)
	elif(c==5):
		obj.find_(str)
	else:
		print("Invalid Input")		