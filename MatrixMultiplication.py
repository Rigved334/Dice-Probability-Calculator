# Matrix Multiplication

# rows and columns input
row1 = int(input("enter number of rows of matrix A: "))
column1 = int(input("enter number of columns of matrix A: "))

row2 = int(input("enter number of rows of matrix B: "))
column2 = int(input("enter number of columns of matrix B: "))

# constraints
if row1 < 1:
    print("invalid for rows")
elif column1 < 1:
    print("invalid for columns")

if row2 < 1:
    print("invalid for rows")
elif column2 < 1:
    print("invalid for columns")

if row1 < column2:
    print("cannot perform operation")
elif row2 < column1:
    print("cannot perform operation")

# Element input
print("enter the elements of matrix A")
A = []
for i in range(row1):
    row = []
    for j in range(column1):
        a = float(input("enter the elements row-wise: "))
        row.append(a)
    A.append(row)

print("\nenter the elements of matrix B")
B = []
for i in range(row2):
    row = []
    for j in range(column2):
        b = float(input("enter the elements row-wise: "))
        row.append(b)
    B.append(row)

C = []
for i in range(row1):
    c = [0] * column2
    C.append(c)

# Multiplication
for i in range(row1):
    for j in range(column2):
        for k in range(column1):
            C[i][j] += A[i][k] * B[k][j]

for row in C:
    print(row)

hello