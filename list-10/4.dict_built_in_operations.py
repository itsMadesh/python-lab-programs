# dictionary-built-in-functions.
print("MENU:\n1.clear()\n2.copy()\n3.fromkeys()\n4.get()\n5.items()\n6.keys()\n7.pop()\n8.popitem()\n9.setdefault()\n10.update()\n11.values()")
c = "y"
while(c == "y"):
    choice = int(input("Enter a choice:"))
    if(choice == 1):
        student_details = {"Name": "Madesh", "Age": 18,
                           "Branch": "IT", "Sec": "S2", "Roll.no": "S02031"}
        student_details.clear()
        print(student_details)
    elif(choice == 2):
        student_details = {"Name": "Madesh", "Age": 18,
                           "Branch": "IT", "Sec": "S2", "Roll.no": "S02031"}
        x = student_details.copy()
        print(x)
    elif(choice == 3):
        x = ("Name",)
        y = ("Madesh")
        z = dict.fromkeys(x, y)
        print(z)
    elif(choice == 4):
        student_details = {"Name": "Madesh", "Age": 18,
                           "Branch": "IT", "Sec": "S2", "Roll.no": "S02031"}
        x = student_details.get("Age")
        print(x)
    elif(choice == 5):
        student_details = {"Name": "Madesh", "Age": 18,
                           "Branch": "IT", "Sec": "S2", "Roll.no": "S02031"}
        print(student_details.items())
    elif(choice == 6):
        student_details = {"Name": "Madesh", "Age": 18,
                           "Branch": "IT", "Sec": "S2", "Roll.no": "S02031"}
        print(student_details.keys())
    elif(choice == 7):
        student_details = {"Name": "Madesh", "Age": 18,
                           "Branch": "IT", "Sec": "S2", "Roll.no": "S02031"}
        print(student_details.pop("Age"))
    elif(choice == 8):
        student_details = {"Name": "Madesh", "Age": 18,
                           "Branch": "IT", "Sec": "S2", "Roll.no": "S02031"}
        print(student_details.popitem())
    elif(choice == 9):
        student_details = {"Name": "Madesh", "Age": 18,
                           "Branch": "IT", "Sec": "S2", "Roll.no": "S02031"}
        print(student_details.setdefault("sem", 1))
    elif(choice == 10):
        student_details = {"Name": "Madesh", "Age": 18,
                           "Branch": "IT", "Sec": "S2", "Roll.no": "S02031"}
        student_details.update({"Sem": 1})
        print(student_details)
    elif(choice == 11):
        student_details = {"Name": "Madesh", "Age": 18,
                           "Branch": "IT", "Sec": "S2", "Roll.no": "S02031"}
        print(student_details.values())
    else:
        print("INVALID CHOICE")
    c = input("Do you want to continue(y/n):")
