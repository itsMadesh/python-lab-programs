#6. Write a Python program to copy the contents of a file to another file . 

from shutil import copyfile 
copyfile("lab-7/factorial.py", 'abc.py') 
f=open("abc.py","r")
a=f.readlines()
for i in a:
    print(i,end="")
