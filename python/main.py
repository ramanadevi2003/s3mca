rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

A = []
B = []

print("Enter elements of Matrix A:")
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    A.append(row)

print("Enter elements of Matrix B:")
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    B.append(row)

print("\nAddition:")
for i in range(rows):
    for j in range(cols):
        print(A[i][j] + B[i][j], end=" ")
    print()

print("\nSubtraction:")
for i in range(rows):
    for j in range(cols):
        print(A[i][j] - B[i][j], end=" ")
    print()

print("\nMultiplication:")
for i in range(rows):
    for j in range(cols):
        print(A[i][j] * B[i][j], end=" ")
    print()

print("\nDivision:")
for i in range(rows):
    for j in range(cols):
        if B[i][j] != 0:
            print(A[i][j] / B[i][j], end=" ")
        else:
            print("Undefined", end=" ")
    print()