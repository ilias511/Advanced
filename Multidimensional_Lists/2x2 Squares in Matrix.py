def read_matrix():
    ro,col = [int(x) for x in input().split()]

    matrix = [

    ]
    for i in range(ro):
        elements = [x for x in input().split(' ')]
        matrix.append(elements)

    return matrix



my_matrix = read_matrix()

lines = len(my_matrix)
rows = len(my_matrix[0])
matches = 0
for i in range(0,lines-1):
    for j in range(0,rows-1):
        left_symbol = my_matrix[i][j]
        right_symbol = my_matrix[i][j+1]
        down_left = my_matrix[i+1][j]
        down_right = my_matrix[i+1][j+1]
        if left_symbol==right_symbol==down_right==down_left:
            matches+=1


print(matches)