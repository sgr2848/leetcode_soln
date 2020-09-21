def zero_matrix(m, n):
    return [[0]*m]*n
def get_one_square(M):
    row = len(M)
    col = len(M[0])
    new_M = zero_matrix(row+1, col+1)
    max_len = 0
    for i in range(1, row):
        for j in range(1, col):
            if M[i - 1][j - 1] == 1:
                new_M[i][j] = min(min(new_M[i][j - 1], new_M[i - 1][j]), new_M[i - 1][j - 1]) + 1
                print(
                    f'| {new_M[i][j - 1]} - {new_M[i - 1][j]} - {new_M[i - 1][j - 1]}|', end=" -")
                max_len = max(max_len, new_M[i][j])
        print()
    print(new_M)
    return f'{max_len}x{max_len}'
    
M = [[1, 1, 1, 1, 1],
     [1, 1, 1, 1, 0],
     [1, 1, 1, 1, 0],
     [1, 1, 1, 1, 0],
     [1, 1, 1, 1, 1],
     [0, 0, 0, 0, 0]]
print(get_one_square(M))
