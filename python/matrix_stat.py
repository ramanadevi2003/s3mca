import numpy as np


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


print("\nSum of all elements:", np.sum(A))
print("Mean of all elements:", np.mean(A))
print("Maximum element:", np.max(A))
print("Minimum element:", np.min(A))