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
