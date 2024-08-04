matrix = []
for i in range(9):
    matrix.append(list(map(int, input().split((' ')))))

max_val = 0
max_idx = [0, 0]
for i in range(9):
    for j in range(9):
        if matrix[i][j] > max_val:
            max_val = matrix[i][j]
            max_idx = [i, j]

print(max_val)
print(str(max_idx[0] + 1) + ' ' + str(max_idx[1] + 1))