import sys
if(len(sys.argv) == 4):
    a=int(sys.argv[1])
    b=sys.argv[2]
    c=int(sys.argv[3])
    if(b=="+"):
        print(a,b,c,"=",a+c) 
    elif(b=="-"):
        print(a,b,c,"=",a-c)    
    elif(b=="*"): 
        print(a,b,c,"=",a*c) 
    elif(b=="%"):
        print(a,b,c,"=",a%c) 
    elif(b=="/"):
        print(a,b,c,"=",a/c) 
    else:
        print("Invalid expression")                    
else:
    print("Invalid arguments")

