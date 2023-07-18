# Read the dimensions of the matrices
temp = input().split(' ')
m, n = int(temp[0]), int(temp[1])

# Read the first matrix
a = []
for i in range(m):
    row = list(map(int, input().split()))
    a.append(row)

# Read the second matrix
b = []
for i in range(m):
    row = list(map(int, input().split()))
    b.append(row)

# Compute the sum of the matrices
result_matrix = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(a[i][j] + b[i][j])
    result_matrix.append(row)

# Print the result matrix
for row in result_matrix:
    print(' '.join(str(x) for x in row))