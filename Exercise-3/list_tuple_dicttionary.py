#Aim: to write programs on functions of lists,tuples and dictionaries.
#1. Write a program which will find all such numbers which are divisible by 7 but
#are not a multiple of 5, between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a
#single line.

n=[]
for i in range(2000,3201):
    if((i%7==0) and (i%5!=0)):
        n.append(str(i))
print((",").join(n))        


#2. Write a program which can compute the factorial of a given numbers.
#The results should be printed in a comma-separated sequence on a single line.

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
fact_number=int(input("Enter a number:"))
print("factorial of a given number is",fact(fact_number))


#3. Write a program that accepts a comma separated sequence of words as input
#and prints the words in a comma-separated sequence after sorting them
#alphabetically.

a=input("Enter a string:")
b=a.split()
print("unsorted words:",b)
b.sort()
print("sorted words:",b)

#4.Write a program that accepts sequence of lines as input and prints the lines
#after making all characters in the sentence capitalized
a=input("Enter a string:")
b=a.upper()
print("After captilalized all the character in a given string:",b)

#5.Write a program that accepts a sequence of whitespace separated words as input
#and prints the words after removing all duplicate words and sorting them
#alphanumerically. 

a=input("Enter a string:")
b=a.split( )
c={}
print(b)
for i in b:
      if i not in c:
          c.append(i)    
      continue 
c.sort()
print((" ").join(c))

# 6. Write a program which accepts a sequence of comma separated 4 digit binary
# numbers as its input and then check whether they are divisible by 5 or not. The
# numbers that are divisible by 5 are to be printed in a comma separated sequence.

items = []
num = [x for x in input().split(',')]
for p in num:
    x = int(p, 2)
    if not x%5:
        items.append(p)
print(','.join(items))


#7.Write a program, which will find all such numbers between 1000 and 3000
#(both included) such that each digit of the number is an even number.
#The numbers obtained should be printed in a comma-separated sequence on a
#single line

numbers = []
for i in range(1000, 3001):
    num=i
    while(i > 0):
        s = i % 10
        if(s % 2 != 0):
            break
        i = i//10
    else:
        numbers.append(num)
print(numbers)

#8. Write a program that accepts a sentence and calculate the number of letters and digits.

sentence=input("Type sentence:")
letters=0
for i in sentence:
    if i not in (" "):
       letters+=1
print("letters:",letters)       
digits=sentence.split()
print(len(digits))     

#9. A website requires the users to input username and password to register. Write
#a program to check the validity of password input by user.

import re 
def password(i):      
        if (len(i)<6 or len(i)>12): 
            return False
        elif not re.search("[a-z]",i): 
            return False
        elif not re.search("[0-9]",i): 
            return False
        elif not re.search("[A-Z]",i):
            return False
        elif not re.search("[$#@]",i):
            return False 
        elif re.search("\s",i): 
            return False 
        else: 
            return True 
passwords=[]
for i in range(3):
    a=input("Enter a password-"+str(i+1)+":")
    passwords.append(a)
valid=[]    
for i in passwords:
    if (password(i)==True):
        valid.append(i)
print("valid passwords:",(",").join(valid))


#10. You are required to write a program to sort the (name, age, height) tuples by
#ascending order where name is string, age and height are numbers. The tuples are
#input by console. The sort criteria is:
#1: Sort based on name;
#2: Then sort based on age;
#3: Then sort by score.
#The priority is that name > age > score.

from  operator import itemgetter

list1=[]
for i in range(4):
    a=input("Enter a Name , Age and height with whitespaces:")
    b=tuple(a.split(" "))
    list1.append(b)
print("unsorted:",list1)  
list1.sort(key=itemgetter(0,1,2))
print("sorted:",list1)

#11. Write a program to compute the frequency of the words from the input. The
#output should output after sorting the key alphanumerically. 

text_line = input("Enter the string: ") 
freq_dict = {} 
for i in text_line.split(): 
    if i not in freq_dict: 
        freq_dict[i] = 1 
    elif i in freq_dict: 
        freq_dict[i] = freq_dict[i] + 1 
sorted_freq_dict = sorted(freq_dict.items()) 
print(sorted_freq_dict)
for i in sorted_freq_dict: 
    print(i[0],":", i[1]) 


#12. Define a function that can accept two strings as input and print the string with
#maximum length in console. If two strings have the same length, then the function
#should print all strings line by line. 

def printstring(s1,s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1>len2:
       print(s1)
    elif len2>len1:
       print(s2)
    else:
       print(s1)
       print(s2)
s1=input("Enter a string 1:")
s2=input("Enter a string 2:")
printstring(s1,s2)

# 13. Define a function which can generate a dictionary where the keys are numbers
# between 1 and 20 (both included) and the values are square of keys. The function
# should just print the values only.


def printvalue():
    a = dict()
    for i in range(1, 21):
        a[i] = i**2
    for i in a:
        print("values:", a[i])
printvalue()

# 14.Write a program to generate and print another tuple whose values are even
# numbers in the given:tuple (1,2,3,4,5,6,7,8,9,10).

tuple1 = tuple()
l1 = []
main = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for i in main:
    if i % 2 == 0:
        l1.append(i)
tuple1 = tuple(l1)
print("Even numbers:",tuple1)

#15. Write a program which can filter even numbers in a list by using filter
#function. The list is:[1,2,3,4,5,6,7,8,9,10].

list1=[1,2,3,4,5,6,7,8,9,10]
evennumbers=list(filter(lambda x:x%2==0, list1))
print(evennumbers)

#16. Write a program which can map() to make a list whose elements are square
#of elements in [1,2,3,4,5,6,7,8,9,10]. 

list1=[1,2,3,4,5,6,7,8,9,10]
square_numbers=list(map(lambda x:x**2, list1))
print(square_numbers)

#17. Write a program which can map() and filter() to make a list whose elements
#are square of even number in [1,2,3,4,5,6,7,8,9,10]. 

list1 = [1,2,3,4,5,6,7,8,9,10]
even_numbers_square = list(map(lambda x: x**2, filter(lambda x: x%2==0, list1)))
print(even_numbers_square)

#18. Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by
#console (n>0).

n=int(input("Enter a number:"))
s=0
for i in range (1,n+1):
    s=s+i/(i+1) 
print(float(s))         

#19. Write a program to compute:f(n)=f(n-1)+100 when n>0 and f(0)=1 with a given n input by console (n>0).

def f(n):
    if n==0:
        return 0
    return f(n-1)+100   
n=int(input("Enter a number:")) 
print(f(n))

#20. Write a binary search function which searches an item in a sorted list. The
#function should return the index of element to be searched in the list. 
def binarysearch(a,l,r,key):
    while(l<=r):
        mid=l+(r-l)//2
        if(a[mid]==key):
            return "Element found in index-"+str(mid)
        elif(key>a[mid]):
            l=mid+1
        else:
            r=mid-1 
    return "not found"           
a=[]
n = int(input("how a many elements do you want to include into your list:"))
for i in range(n):
    b = input("Enter element-"+str(i+1)+":")
    a.append(int(b))
a.sort()    
print(a)
search_key = int(input("Enter a search value:"))
print(binarysearch(a, 0, n-1, search_key))

#21. Generate a random float where the value is between 10 and 100 using Python
#math module

import random 
n = int(input("Enter the number of random float values needed: ")) 
for x in range(n): 
    print(random.uniform(10, 101)) 

#22.Write a program to output a random number, which is divisible by 5 and 7,
#between 0 and 10 inclusive using random module and list comprehension. 

import random
print (random.choice([i for i in range(10,151) if i%5==0 and i%7==0])) 

#23.Write a program to generate a list with 5 random numbers between 100 and
#200 inclusive. 

import random
print(random.sample(range(100,201),5))

 
