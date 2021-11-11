# 3. Get 2 string matrices of size M*M and N*N. Perform padding to make it equal in size 
# and do any one conventional string operation on the resultant matrix.
# m=int(input("Enter m value:"))
# n=int(input("Enter n value:"))
# m1=[]
# m2=[]
# print("Enter strings in matrix-1:")
# for i in range(m):
#     str=input("Enter string-{}:".format(i+1))
#     m1.append(str)
# print("Enter strings in matrix-2:")
# for i in range(n):
#     str=input("Enter string-{}:".format(i+1))
#     m2.append(str)  
# print(m1)
# print(m2)     
 
def createMatrix(size):
    """ Creates a string matrix of given size"""
    m = []
    print("Enter elements of the matrix in the format you write in your notebook:")
    for i in range(size):
        n=[k for k in input().split()][:size]
        m.append(n)
    return m

def padding(matrix, size):
    """ Add space in the string matrix to equalize it with a given size"""
    diff = size - len(matrix)
    for l in matrix:
        l.extend(diff * [" "])
    for j in range(diff):
        matrix.append([" " for k in range(size)])    
def matrixAddition(A, B):
    """ Concatenation of two matrice A and B"""
    C = []
    for i in range(len(A)):
        d = []
        for j in range(len(A)):
            d.append(A[i][j] + B[i][j])
        C.append(d)
    return C

def matrixDisplay(A):
    """ Displays the given matrix"""
    for i in range(len(A)):
        for j in range(len(A)):
            print(A[i][j],end=" ")
        print()
    
#main

m = int(input("Enter size of matrix A: "))
A = createMatrix(m)
print(A)

n = int(input("Enter size of matrix B: "))
B = createMatrix(n)
print(B)

if m > n:
    padding(B, m)
else:
    padding(A, n)
    
print("Matrix addition after padding the given matrices:")
matrixDisplay(matrixAddition(A,B))