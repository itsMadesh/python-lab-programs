# 3. WAP to calculate and display the Net salary of an employee from his/her gross salary. Deduct taxes as
# appropriate. Get the gross salary as input from the user.

g = int(input("Enter a gross salary :"))
tax_percentage = 0.05 if g < 100000 else 0.10
tax = g*tax_percentage
net_salary = g-tax
print("Net salary is", net_salary)

# This program got executed succesfully and the output has been verified
