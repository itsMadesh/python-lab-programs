def addition(a, b, r1, c1, r2, c2):
    if((r1 != r2 and (r2 != c2))):
        return "matrix addition does not exits for given matrices"
    ans = [[0 for j in range(c2)] for i in range(r1)]
    for i in range(r1):
        for j in range(r1):
            ans[i][j] = a[i][j]+b[i][j]
    return ans


def subraction(a, b, r1, c1, r2, c2):
    if((r1 != r2 and (c1 != c2))):
        return "matrix subraction does not exits for given matrices"
    ans = [[0 for j in range(c2)] for i in range(r1)]
    for i in range(r1):
        for j in range(r1):
            ans[i][j] = a[i][j]-b[i][j]
    return ans


def multiplication(a, b, r1, c1, r2, c2):
    if(c1 != r2):
        return "matrix multiplication does not exits for given matrices"
    ans = [[0 for j in range(c2)] for i in range(r1)]
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                ans[i][j] += a[i][k]*b[k][j]
    return ans


def getInput(m, r, c):
    return [[int(input("Enter a value in "+m+"["+str(i)+"]["+str(j)+"]:"))
             for j in range(c)] for i in range(r)]


def getRowCol(m):
    return int(input("Enter a row for matrix-"+m+":")), int(input("Enter a col for matrix-"+m+":"))


def printMatrix(s, m):
    print("Matrix-"+s+":")
    for i in range(len(m)):
        print(m[i])


def printOutput(s, ans):
    if(type(ans) == list):
        printMatrix(s, ans)
    else:
        print(ans)


while(True):

    print("choices:\n", "1.matrix additon \n", "2.matrix subraction \n",
          "3.matrix multiplication \n", "4.exit")
    choice = int(input("Enter a choice(1/2/3/4):"))

    if(choice == 4):
        break

    elif((choice == 1) or choice == 2 or choice == 3):

        r1, c1 = getRowCol("A")
        a = getInput("a", r1, c1)
        printMatrix("A", a)

        r2, c2 = getRowCol("B")
        b = getInput("b", r2, c2)
        printMatrix("B", b)

        if(choice == 1):
            add = addition(a, b, r1, c1, r2, c2)
            printOutput("(A+B)", add)
        elif(choice == 2):
            sub = subraction(a, b, r1, c1, r2, c2)
            printOutput("(A-B)", sub)
        elif(choice == 3):
            multi = multiplication(a, b, r1, c1, r2, c2)
            printOutput("(A*B)", multi)

    else:
        print("Invalid choice")
