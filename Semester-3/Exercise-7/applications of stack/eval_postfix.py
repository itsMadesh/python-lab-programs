from stack import Stack
def evaluate(exp):
	s=Stack()
	print("%s\t%10s\t%20s"%("Char","Stack","Evaluation"))
	for i in exp:
		if(i.isdigit()):
			s.push(i)
		else:
			a=s.pop()
			b=s.pop()
			if(i=='^'):
				i='**'
			s.push(str(eval(b+i+a))	)
	return s.pop()
exp=input("Enter postfix expression:")
print(exp,"is equal to",evaluate(exp))