import numpy as np

# Input rows and columns
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter the matrix elements:")

matrix = []
for i in range(rows):
    while True:
        row = list(map(int, input().split()))
        if len(row) == cols:
            matrix.append(row)
            break
        else:
            print(f"Please enter exactly {cols} elements.")

A = np.array(matrix)

print("\nOriginal Matrix:")
print(A)

# Rotate 90 degrees clockwise
print("\nMatrix Rotated 90° Clockwise:")
print(np.rot90(A, -1))

# Rotate 180 degrees
print("\nMatrix Rotated 180°:")
print(np.rot90(A, 2))

# Rotate 270 degrees clockwise
print("\nMatrix Rotated 270° Clockwise:")
print(np.rot90(A, -3))