#i. Use nested list and print the contents

a = [[int(input("Enter a value in a["+str(i)+"]["+str(x)+"]:"))
      for x in range(3)] for i in range(3)]
[[print(a[i][j],end=" ") for j in range(3)] for i in range(3)]



