# 1. WAP to convert temperature centigrade to Fahrenheit and vice-versa. Get the input data from the user
# as appropriate.

c = float(input('Enter a celsius :'))
f = (1.8*c)+32
print("Farenheit is", f)
f = float(input("Enter a farenheit :"))
c = (f-32)/1.8
print("Celsius is", c)

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 2. Write the necessary input and output statement for each of the following situations:
# (a) Generate the messages.
# Enter your name:
# Enter your register number:
# Enter the current semester you belong to:
# Then enter the appropriate value. Assign the values to approrpriate types and then print them

name = input("Enter your name :")
reg_num = input("Enter your register number :")
sem = input("Enter the current semester you belong to :")

# (b) Suppose x and y are integer variables, prompt the user to enter values for these
# two variables and then display their product. Label the output as appropriate.

x = int(input("Enter a number-1:"))
y = int(input("Enter a number-2:"))
print("Multiplied", x, "by", y, "is equal to", x*y)

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 3. WAP to calculate and display the Net salary of an employee from his/her gross salary. Deduct taxes as
# appropriate. Get the gross salary as input from the user.

g = int(input("Enter a gross salary :"))
tax_percentage = 0.05 if g < 100000 else 0.10
tax = g*tax_percentage
net_salary = g-tax
print("Net salary is", net_salary)

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 4. WAP to display the ASCII value of a char got as input from the user and vice versa.

char = input("Enter a character :")
ascii_value = ord(char)
print("Ascii value of", char, "is", ascii_value)
ascii_value = int(input("Enter a ascii value :"))
char = chr(ascii_value)
print("character of ", ascii_value, "is", char)

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 5. Write a Program to check whether a given number is even or odd

n = abs(int(input("Enter a number :")))
if(n % 2 == 0):
    print("Given number is even")
else:
    print("Given number is odd")

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 6. Write a Program to find whether a given year is a leap year or not.

a = int(input("enter a year : "))
if((a % 400 == 0) or ((a % 4 == 0) and (a % 100 != 0))):
    print(a, " is a leap year")
else:
    print(a, " is not a leap year")

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 7. Write a Program to read the age of a candidate and determine whether it is eligible for casting his/her own vote.

age = int(input("Enter an age of a canditate :"))
if(age >= 18):
    print("This canditate is eligible for voting")
else:
    print("This canditate is not eligible fot voting")

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 8. Write a Program to accept the height of a person entimeter and categorize the person according to their height.

h = float(input("Enter the height of a person(in centimeter) :"))
if(h < 150):
    print("The person is dwarf")
elif(h >= 150 and h < 175):
    print("The person is averge height")
elif(h >= 175 and h < 195):
    print("The person is tall")
else:
    print("The person is very tall")

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 9. Write a Program to find the largest of three numbers.

a = int(input("Enter a first number :"))
b = int(input("Enter a second  number :"))
c = int(input("Enter a third number :"))
if(a > b and a > c):
    print(a, "is largest ")
elif(b > a and b > c):
    print(b, "is largest ")
else:
    print(c, "is largest ")

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 10. Write a Program to calculate the roots of a Quadratic Equation.

import math
a = int(input("Enter a number a :"))
b = int(input("Enter a number b :"))
c = int(input("Enter a number c :"))
d = b*b-4*a*c
if(d >= 0):
    root1 = (-b+math.sqrt(d))/2*a
    root2 = (-b-math.sqrt(d))/2*a
    print("roots are", root1, ",", root2)
else:
    print("roots are imaginary")

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 11. Write a Program to read roll no, name and marks of three subjects and calculate the total, percentage and grade.

roll_no = input("Enter a roll_no of the student :")
name = input("Enter a name of the student :")
sub1_mark = int(input("Enter a mark of the subject-1 :"))
sub2_mark = int(input("Enter a mark of the subject-2 :"))
sub3_mark = int(input("Enter a mark of the subject-3 :"))
total_mark = sub1_mark+sub2_mark+sub3_mark
print("Total mark is", total_mark)
percentage = total_mark/3
print("Percentage is", percentage)
if(percentage > 80 and percentage <= 100):
    print("Grade is A")
elif(percentage > 60 and percentage <= 80):
    print("Grade is B")
elif(percentage >= 35 and percentage <= 60):
    print("Grade is c")
else:
    print("fail")

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 12. Write a Program to read temperature entigrade and display a suitable message according to temperature state below:
# Temp < 0 then Freezing
# Temp 0-10 then Very Cold
# Temp 10-20 then Cold
# Temp 20-30 then Normal
# Temp 30-40 then Hot
# Temp >=40 then Very Hot

temp = float(input("Enter a temperature centigrade :"))
if(temp < 0):
    print("Temperature state: Freezing")
elif(temp > 0 and temp < 10):
    print("Temperature state: Very cold")
elif(temp >= 10 and temp < 20):
    print("temperature state: Cold")
elif(temp >= 20 and temp < 30):
    print("Temperature state: Normal")
elif(temp >= 30 and temp < 40):
    print("Temperature state: Hot")
else:
    print("temperature state: very hot")

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 13. Write a Program to check whether a character is an alphabet, digit or special character.

char = input("Enter a character:")
if char.isalpha():
    print("Given character is a alphabet")
elif char.isdigit():
    print("Given character is a digit")
else:
    print("Given character is a special character")

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 14. Write a Program to check whether an alphabet is a vowel or consonant.

char = input("Enter a alphabet :")
if not char.isalpha():
    print("Invalid input")
elif char in ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'):
    print(char, "is a vowel")
else:
    print(char, "is a consonant")

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
#15. Write a program to read any digit, display in the word.

digit=input("Enter a digit :")
word={'0':'Zero','1':'One','2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'seven','8':'Eight','9':'Nine'}
print(word[digit])

# This program got executed successfully and the output has been verified.
#==============================================================================================================#
# 16. Write a program to read any Month Number in integer and display the number of days for this month.

n = int(input("Enter any month in integer:"))
month_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31,
              6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
print("Given month have", month_days[n], "days")

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 17. Write a program for a simple calculator.

while(True):
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.exit")
    c = int(input("Enter a choice no:"))
    if(c < 1 or c > 5):
        print(" Invalid input ")
        continue
    elif(c == 5):
        break
    a = float(input("Enter a number a : "))
    b = float(input("Enter a number b : "))
    if(c == 1):
        print(a, "+", b, "=", a+b)
    elif(c == 2):
        print(a, "-", b, "=", a-b)
    elif(c == 3):
        print(a, "*", b, "=", a*b)
    elif(c == 4):
        print(a, "/", b, "=", a/b)

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 18. (a).This program will prints all odd numbers between 10 and 60.
print("odd numbers between 10 and 60 are ", end="")
for i in range(10, 61):
    if(i % 2 != 0):
        print(i, end=" ")

# (b).This program will prints all the numbers between 1 and 50,with 10 numbers on each line with all the columns aligned with proper spaces.
print("\nAll the numbers between 1 and 50 are ")
for i in range(1, 51):
    if i % 10 == 0:
        print(i, end="\n")
    else:
        if(i < 10):
            print('0'+str(i), end=" ")
        else:
            print(i, end=" ")


# (c).This program will get a number from user and prints the number muliplied by 10.Repeat until 0 is entered.
n = 1
while(True):
    n = int(input("Enter a number :"))
    if n == 0:
        break
    print(n, "is multiplied by 10 :", n*10)


# This program got executed successfully and the output has been verified.
#==============================================================================================================#
# 19. Write a program to generate n pseudo random generators.

import random

n = int(input("Enter n : "))

for i in range(n):
    print(random.random())

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 20. Write a program to read n number of values in an list and display it in reverse order.

n = int(input("How many elements do you want to include into list :"))
list_1 = []
print("Enter any", n, "list elements :")
for i in range(0, n, 1):
    a = int(input())
    list_1.append(a)
print("Original list is", list_1)
i = -1
reverse_order = []
while(i >= -n):
    a = list_1[i]
    reverse_order.append(a)
    i = i+-1
print(reverse_order)

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 21. Write a program to find the sum of all elements of the list.

list = [1, 2, 3, 4, 5]
n = len(list)
sum = 0
for i in range(0, n):
    sum = sum+list[i]
print("Sum of all the list elements is", sum)

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
#22. Write a program to copy the elements of one list into another list. 

list_1=[1,2,3,4,5]
list_2=list_1.copy()
print("Copied list is ",list_2)

# This program got executed successfully and the output has been verified.
#==============================================================================================================#
# 23. Write a program to count a total number of duplicate elements in an list.

num = []
n = int(input("How many elements do you want to inclued into list:"))
print("Enter a list elements :")
for i in range(0, n):
    a = int(input())
    num.append(a)
print("Given list is",num)
unique_elements = []
for i in range(0, n):
    if(num[i] not in unique_elements):
        unique_elements.append(num[i])
print("Total number of duplicate elements in list are :",len(num)-len(unique_elements))

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 24. Write a program to print all unique elements in an list.

num = []
n = int(input("How many elements do you want to inclued into list:"))
print("Enter a list elements :")
for i in range(0, n):
    a = int(input())
    num.append(a)
print("Given list is ",num)
unique_elements = []
for i in range(0, n):
    if(num[i] not in unique_elements):
        unique_elements.append(num[i])
print("Unique elements in list :",unique_elements)

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 25. Write a program to merge two lists of same size sorted in decending order.

list_1 = []
list_2 = []
n = int(input("How many elements do you want to inclued into list:"))
print("Enter a list-1 elements :")
for i in range(0, n):
    a = int(input())
    list_1.append(a)
print("list-1 is ", list_1)
print("Enter a list-2 elements :")
for i in range(0, n):
    a = int(input())
    list_2.append(a)
print("list-2 is ", list_2)
merge_list = list_1+list_2
print("Merged list:",merge_list)
merge_list.sort(reverse=True)
print("Merged list in descending order :",merge_list)

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 26. Write a program to count the frequency of each element of an list.

n = int(input("How many elements do you want to include into list :"))
arr = []
print("Enter any", n, "list elements :")
for i in range(0, n):
    a = int(input())
    arr.append(a)
print("List is ", arr)
unique_arr = list(set(arr))
for i in range(0, len(unique_arr)):
    print("Frequency of element",
          unique_arr[i], " is", arr.count(unique_arr[i]))

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 27. Write a program to find the maximum and minimum element in an list .

n = int(input("Enter size of list : "))
arr = []
for i in range(n):
    arr.append(int(input("Enter element :")))
print("Minimum in list : ", min(arr))
print("Maximum in list : ", max(arr))

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 28. Write a program to sort elements of list in ascending order.

n = int(input("Enter size of list : "))
arr = []
for i in range(n):
    arr.append(int(input("Enter element :")))
arr.sort()
print("Sorted list : ", arr)

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 29. Write a program to sort elements of the list in descending order .

n = int(input("Enter size of list : "))
arr = []
for i in range(n):
    arr.append(int(input("Enter element :")))
arr.sort(reverse=True)
print("Sorted list in decending order : ", arr)

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 30. Write a program for multiplication of two square Matrices.


def get_matrix_input(n, name):
    print("Enter values of Matrix ", name, " : ")
    M = []
    for i in range(n):
        M.append([])
        for j in range(n):
            value = int(input("Enter value for i=" +
                              str(i)+" and j="+str(j)+" : "))
            M[i].append(value)
    return M


def print_matrix(M, name):
    print(name, "Matrix : ")
    for r in M:
        print(r)


n = int(input("Enter matrix order : "))

A = get_matrix_input(n, "A")
print_matrix(A, "A")

B = get_matrix_input(n, "B")
print_matrix(B, "B")

result = [[0 for j in range(n)] for i in range(n)]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

print_matrix(result, "Result")

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 31. Write a program to find the length of a string without using library function .

s = input("Enter a string : ")
c = 0
for i in s:
    c = c+1
print("String length : ", c)

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 32. Write a program to separate the individual characters from a string .

s = input("Enter a string : ")
print("Invidual characters of string : ", end="")
for c in s:
    print(c, end=" ")

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 33. Write a program to check if a string is a palindrome.

s = input("Enter a string : ")
rs = s[::-1]
if(s == rs):
    print("String is a palindrome")
else:
    print("String is not a palindrome")

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 34. Write a program to count the total number of words in a string.

s = input("Enter a string : ")
w, f = 0, True
for c in s:
    if(c != ' ' and f):
        w = w+1
        f = False
    elif (c == ' '):
        f = True
print("Count of words is : ", w)

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 35. Write a program to compare two string without using string library functions.

x = input("Enter string-1 : ")
y = input("Enter string-2 : ")


def compare(x, y):
    if(len(x) != len(y)):
        return False
    for i in range(len(x)):
        if(x[i] != y[i]):
            return False
    return True


if(compare(x, y)):
    print("Both strings are equal")
else:
    print("Both strings are not equal")

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 36. Write a program to count total number of alphabets, digits and special characters in a string.

x = input("Enter a string : ")
a, d, s = 0, 0, 0
for c in x:
    if c.isalpha():
        a = a+1
    elif c.isdigit():
        d = d+1
    else:
        s = s+1
print("No of alphabets : ", a)
print("No of digits : ", d)
print("No of special chars : ", s)

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 37. Write a program to count total number of vowel or consonant in a string.

s = input("Enter a string : ")
vc, cc = 0, 0
for c in s:
    if c in ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'):
        vc += 1
    else:
        cc += 1
print("No of vowels : ", vc)
print("No of consonant : ", cc)

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 38. Write a program to find maximum occurring character in a string.

s = input("Enter a string : ")
moc, ch = 0, ""
for c in s:
    if moc < s.count(c):
        moc = s.count(c)
        ch = c
print("maximum occurring character : ", ch)

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 39. Write a program to check whether a given substring is present in the given string.

s = input("Enter a string : ")
ss = input("Enter a sub string : ")
if s.find(ss) == -1:
    print("substring is not present in string")
else:
    print("substring is present in string")

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 40. Write a program to read a sentence and replace lowercase characters by uppercase and vice-versa.

s = input("Enter a string : ")
print("answer string : ", s.swapcase())

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 41. Write a program to find the number of times a given word 'the' appears in the given string.

s = input("Enter a string : ")
print("No of 'the' in string : ", s.count("the"))

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 42. Write a function generateprimes(int limit) to generate all the prime numbers between 2 and some given
# limit and return them as an array. Print all elements from array.

n = int(input("Enter a limit : "))


def generate_primes(n):
    primes = []
    for i in range(2, n+1):
        for j in range(2, i):
            if(i % j == 0):
                break
        else:
            primes.append(i)
    return primes


print("primes within given limit : ", generate_primes(n))

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 43. Write the function int countchars(char string[], int ch) which returns the number of times the character
# ch appears in the string.

s = input("Enter a string : ")
ch = input("Enter a character : ")


def count_chars(s, ch):
    count = 0
    for c in s:
        if c == ch:
            count += 1
    return count


print("No of ", ch, " in string : ", count_chars(s, ch))

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 44. Write the function replace(char string[], char from[], char to[]) which finds the string 'from' in the
# string 'string' and replaces it with the string 'to'.

s = input("Enter a string : ")
f = input("Enter a from string : ")
t = input("Enter a to string : ")


def replace(s, f, t):
    return s.replace(f, t)


print("answer string : ", replace(s, f, t))

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 45. Write a function GCD (greatest common divisor) that accepts two integers and returns -1 if both the
# integers are zero, otherwise it returns their GCD.

a = int(input("Enter a number a :"))
b = int(input("Enter a number b :"))


def find_gcd(a, b):
    if a == 0 and b == 0:
        return -1
    gcd = 1
    for i in range(2, min(a, b)+1):
        if(a % i == 0 and b % i == 0):
            gcd = i
    return gcd


print("Gcd of", a, "and", b, " is", find_gcd(a, b))

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 46. Convert the given decimal number into binary, octal and hexadecimal numbers using user defined functions.

n = int(input("Enter a number : "))


def bin(n):
    s = ""
    while(n):
        s = str(n % 2)+s
        n = n//2
    return s


def oct(n):
    s = ""
    while(n):
        s = str(n % 8)+s
        n = n//8
    return s


def hex(n):
    s = ""
    while(n):
        rem = n % 16
        c = rem if rem < 10 else chr(55+rem)
        s = str(c)+s
        n = n//16
    return s


print("Binary of ", n, " is ", bin(n))
print("Octal of ", n, " is ", oct(n))
print("Hexadecimal of ", n, " is ", hex(n))

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 47. From the given paragraph perform the following using built-in functions:

para = str(input("Type a paragraph :"))
# a. find the total number of words .
total_words = len(para.split())
print("The number of words in a paragraph are", total_words)
# b. capitalise the first word of each sentence
sentences = []
for s in para.split("."):
    sentences.append(s.lstrip().capitalize())
para = ". ".join(sentences)
print("after capitalizion : ", para)
# c. replace a given word with another word
word1 = input("Enter word to be replaced : ")
word2 = input("Enter replacement word : ")
print("After replacing with given word : ", para.replace(word1, word2))

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 49. Write a function with a parameter n that returns the nth Fibonacci number. The function must be recursive.

n = int(input("Enter a number : "))


def fib(n):
    if n <= 1:
        return n
    return fib(n-1)+fib(n-2)


print("fib : ", fib(n))

# This program got executed successfully and the output has been verified.

#==============================================================================================================#
# 50. Write a program that generates 100 random numbers between -0.5 and 0.5 and writes them on screen.

import random
for i in range(100):
    print(random.uniform(-.5, .5))

# This program got executed successfully and the output has been verified.
