limit = int(input("Enter a limit :"))
num = 1
sum = 0
while(num <= limit):
    sum = num+sum
    num = num+1
average = sum/limit
print("The sum of series is ", sum)
print("the average of series is", average)
