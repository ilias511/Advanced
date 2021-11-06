def read_matrix():
    ro, col = [int(x) for x in input().split()]

    matrix = [

    ]
    for i in range(ro):
        elements = [int(x) for x in input().split(' ')]
        matrix.append(elements)

    return matrix


my_matrix = read_matrix()
lines = len(my_matrix)
rows = len(my_matrix[0])
max_sum = 0

row = 0
column = 0
for i in range(0, lines - 2):
    for j in range(0, rows - 2):
        left_symbol = my_matrix[i][j]
        right_symbol = my_matrix[i][j + 1]
        right_symbol_plus_one = my_matrix[i][j + 2]
        down_one = my_matrix[i + 1][j]
        down_one_right = my_matrix[i + 1][j + 1]
        down_one_right_one = my_matrix[i + 1][j + 2]
        down_two = my_matrix[i + 2][j]
        down_two_right = my_matrix[i + 2][j + 1]
        down_two_right_one = my_matrix[i + 2][j + 2]
        all_sum = left_symbol + right_symbol + right_symbol_plus_one + down_one + down_one_right + \
                  down_one_right_one + down_two + down_two_right + down_two_right_one
        if all_sum > max_sum:
            row = i
            column = j
            max_sum = all_sum

print(f'Sum = {max_sum}')
print(my_matrix[row][column], my_matrix[row][column + 1], my_matrix[row][column + 2])
print(my_matrix[row + 1][column], my_matrix[row + 1][column + 1], my_matrix[row + 1][column + 2])
print(my_matrix[row + 2][column], my_matrix[row + 2][column + 1], my_matrix[row + 2][column + 2])
