import numpy as np


rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter the matrix elements:")

matrix = []
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

A = np.array(matrix)

print("\nOriginal Matrix:")
print(A)


print("\nTranspose of Matrix:")
print(A.T)


if rows == cols:
    det = np.linalg.det(A)
    print("\nDeterminant:")
    print(det)

    if det != 0:
        print("\nInverse:")
        print(np.linalg.inv(A))
    else:
        print("\nInverse does not exist (Determinant = 0).")
else:
    print("\nDeterminant and Inverse are possible only for square matrices.")


new_rows = int(input("\nEnter new number of rows for reshape: "))
new_cols = int(input("Enter new number of columns for reshape: "))

if rows * cols == new_rows * new_cols:
    reshaped = A.reshape(new_rows, new_cols)
    print("\nReshaped Matrix:")
    print(reshaped)
else:
    print("\nReshape not possible. Total number of elements must remain the same.")