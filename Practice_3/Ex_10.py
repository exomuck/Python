tmp = input().split(' ')
m, n = int(tmp[0]), int(tmp[1])
# YOUR CODE HERE
matrix = [[i*n + j + 1 for j in range(n)] for i in range(m)]

for row in matrix:
    print(*row)