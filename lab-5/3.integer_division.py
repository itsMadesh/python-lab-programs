c = int(input("Enter a dividing number :"))
a = int(input("Enter a starting range :"))
b = int(input("Enter a ending range :"))
integer_division = []
for i in range(a, b+1):
    d = i//c
    integer_division.append(d)
print("integer division numbers from", a, "to",
      b, "by dividng", c, "is", integer_division)
