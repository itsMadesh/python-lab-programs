from stack import Stack
def Infix_to_Postfix(exp):
    s = Stack()
    p = {'^': 3, '/': 2, '*': 2, '+': 1, '-': 1}
    output = ""
    for i in exp:
        if(i.isalpha() or i.isdigit()):
            output += i
        elif(i == ')'):
            pop_char = s.pop()
            while(pop_char != '('):
                output += pop_char
                pop_char = s.pop()
        else:
            if(s.is_empty() == 1 or i == '('):
                s.push(i)
            elif(s.top() == '(' or p[s.top()] < p[i]):
                s.push(i)
            else:
                while(not s.is_empty() and s.top() != '(' and p[s.top()] >= p[i]):
                    output += s.pop()
                s.push(i)
        # print(output)
    while(not s.is_empty()):
        output += s.pop()
    return output
exp = input("Enter Expression:")
print("Postfix Expression:", Infix_to_Postfix(exp))
