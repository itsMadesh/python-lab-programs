#4. Write a Python program to assess if a file is closed or not. 

f = open("readme.txt",'r') 
print(f.closed) 
f.close() 
print(f.closed) 
