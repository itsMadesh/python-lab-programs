s1 = int(input("Enter a first mark : "))
s2 = int(input("Enter a second mark :"))
s3 = int(input("Enter a third mark :"))
average = (s1+s2+s3)/3
if(average >= 80 and average <= 100):
    print(" first class ")
elif(average >= 60 and average < 80):
    print(" second class ")
elif(average >= 35 and average < 60):
    print(" third class ")
else:
    print(" fail ")
