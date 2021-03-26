import sys
if(len(sys.argv) == 4):
    print("value of a+b*c : ",
          int(sys.argv[1])+int(sys.argv[2])*int(sys.argv[3]))
else:
    print("invalid arguments")
