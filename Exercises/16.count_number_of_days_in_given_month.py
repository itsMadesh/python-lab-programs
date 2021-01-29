# 16. Write a program to read any Month Number in integer and display the number of days for this month.

n = int(input("Enter any month in integer:"))
month_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31,
              6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
print("Given month have", month_days[n], "days")

# This program got executed successfully and the output has been verified.
