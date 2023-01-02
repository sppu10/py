matrixA = []
matrixB = []
matrixC=[[0,0,0],[0,0,0],[0,0,0]]
# Enter the matrix A elements row wise
row = int(input("Enter the number of rows of first matrix: "))
col = int(input("Enter the number of columns of first matrix: "))

print("\nEnter the matrix 'A' elements row wise: ")
for i in range(row):
    a = []

    for j in range(col):
        a.append(int(input()))
    matrixA.append(a)

print("A Matrix elements are: ")
for i in range(row):
    for j in range(col):
        print(matrixA[i][j], end=" ")
    print()

# Enter the matrix B elements row wise
row2 = int(input("\nEnter the number of rows of second matrix: "))
col2 = int(input("Enter the number of column of second matrix: "))

print("\nEnter the matrix 'B' elements row wise: ")
for i in range(row2):
    a = []
    for j in range(col2):
        a.append(int(input()))
    matrixB.append(a)

print("B Matrix elements are: ")
for i in range(row2):
    for j in range(col2):
        print(matrixB[i][j], end=" ")
    print()

# Addition of two matrices
if row == row2 and col == col2:
    resultmatrix = []
    for i in range(row):
        a = []
        for j in range(col):
            a.append(matrixA[i][j] + matrixB[i][j])
        resultmatrix.append(a)

print("\nAddition of two matrices is: ")
for i in range(row):
    for j in range(col):
        print(resultmatrix[i][j], end=" ")
    print()

# Subtraction of two matrices
if row == row2 and col == col2:
    resultmatrix = []
    for i in range(row):
        a = []
        for j in range(col):
            a.append(matrixA[i][j] - matrixB[i][j])
        resultmatrix.append(a)

print("\nSubtraction of two matrices is: ")
for i in range(row):
    for j in range(col):
        print(resultmatrix[i][j], end=" ")
    print()

#Multiplication of two matrices
for i in range(len(matrixA)):
   # iterate through columns of Y
   for j in range(len(matrixB[0])):
       # iterate through rows of Y
       for k in range(len(matrixB)):
           matrixC[i][j] += matrixA[i][k] * matrixB[k][j]
print("\nMultiplication of two matrices is: ")
for r in matrixC:
   print(r)


# Transpose of Matrix A
matrixC = []
for i in range(col):
    a = []
    for j in range(row):
        a.append(0)
    matrixC.append(a)

for i in range(col):
    a = []
    for j in range(row):
        matrixC[i][j] = matrixA[j][i]

print("\nTranspose of Matrix 'A' is: ")
for i in range(col):
    for j in range(row):
        print(matrixC[i][j], end=" ")
    print()

matrixC = []
for i in range(col):
    a = []
    for j in range(row):
        a.append(0)
    matrixC.append(a)

for i in range(col):
    a = []
    for j in range(row):
        matrixC[i][j] = matrixB[j][i]

print("\nTranspose of Matrix 'B' is: ")
for i in range(col):
    for j in range(row):
        print(matrixC[i][j], end=" ")
    print()
