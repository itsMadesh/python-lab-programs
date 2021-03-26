with open("file1.txt") as file1, open("file2.txt") as file2:
    f1=file1.read()
    f2=file2.read()
file1.close()
file2.close()    
with open("file3.txt","w") as file3:
    file3.write(f1+f2)
file3.close()
def file_size(fname): 
   import os 
   statinfo = os.stat(fname) 
   return statinfo.st_size 
print("file size of the resultant file: ",file_size("file3.txt"))
