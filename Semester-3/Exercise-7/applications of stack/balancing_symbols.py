import stack
def balancing(exp):
    s = stack.Stack()
    for i in exp:
        if(i == '(' or i == '[' or i == '{'):
            s.push(i)
        else:
            c = s.pop()
            if(c == '('):
                if(i != ')'):
                    return False
            elif(c == '['):
                if(i != ']'):
                    return False
            elif(c == '{'):
                if(i != '}'):
                    return False
    return True


exp = input("Enter a string:")
if(balancing(exp)):
    print("Balanced")
else:
    print("Unbalanced")
