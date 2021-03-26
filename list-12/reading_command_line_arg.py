# 1. Develop programs to perform any task by reading arguments from command line.


import sys 
ct=0 
for word in sys.argv[1].split(): 
    ct=ct+1 
print (ct) 
