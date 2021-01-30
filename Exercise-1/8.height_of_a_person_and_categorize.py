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
