# 1. WAP to convert temperature centigrade to Fahrenheit and vice-versa. Get the input data from the user
# as appropriate.

c = float(input('Enter a celsius :'))
f = (1.8*c)+32
print("Farenheit is", f)
f = float(input("Enter a farenheit :"))
c = (f-32)/1.8
print("Celsius is", c)

# This program got executed successfully and the output has been verified.
