matrix_size = list(map(int,input().split(' ')))

matrix_A = []
for i in range(matrix_size[0]):
    matrix_A.append(list(map(int, input().split(' '))))
matrix_B = []
for i in range(matrix_size[0]):
    matrix_B.append(list(map(int, input().split(' '))))

matrix_Result = []
for i in range(matrix_size[0]):
    matrix_Result_row = []
    for j in range(matrix_size[1]):
        matrix_Result_row.append(matrix_A[i][j] + matrix_B[i][j])
    matrix_Result.append(matrix_Result_row)

for i in range(matrix_size[0]):
    for j in range(matrix_size[1]):
        print(matrix_Result[i][j], end='')
        if j < matrix_size[1] - 1:
            print(' ', end='')
        else:
            print('')