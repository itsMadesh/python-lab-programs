# 3. Dictionary comprehension and membership

a = {input("enter key : "): input("enter value : ") for i in range(3)}
print(a)
if "madesh" in a:
    print("madesh is in dictionary-a")
else:
    print("madesh is not in dictionary-a")
