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

print("\nVertical Flip:")
print(np.flipud(A))

print("\nHorizontal Flip:")
print(np.fliplr(A))

print("\nFlip Both:")
print(np.flip(A))