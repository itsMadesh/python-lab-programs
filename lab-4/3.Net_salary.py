days = int(input("Enter the total days present :"))
wages = int(input("Enter the wages per day :"))
tax = int(input("Enter tax :"))
basic = wages*days
hra = basic*0.30
transport = basic*0.10
medical = basic*0.10
g = basic+hra+transport+medical
salary = g-tax
print("basic :", basic)
print("hra :", hra)
print("transport:", transport)
print("medical:", medical)
print("Gross salary :", g)
print("Net salary :", salary)
