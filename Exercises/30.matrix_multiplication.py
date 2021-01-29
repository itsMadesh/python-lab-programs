# 30. Write a program for multiplication of two square Matrices.


def get_matrix_input(n, name):
    print("Enter values of Matrix ", name, " : ")
    M = []
    for i in range(n):
        M.append([])
        for j in range(n):
            value = int(input("Enter value for i=" +
                              str(i)+" and j="+str(j)+" : "))
            M[i].append(value)
    return M


def print_matrix(M, name):
    print(name, "Matrix : ")
    for r in M:
        print(r)


n = int(input("Enter matrix order : "))

A = get_matrix_input(n, "A")
print_matrix(A, "A")

B = get_matrix_input(n, "B")
print_matrix(B, "B")

result = [[0 for j in range(n)] for i in range(n)]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

print_matrix(result, "Result")

# This program got executed successfully and the output has been verified.
