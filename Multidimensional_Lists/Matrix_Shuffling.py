def read_matrix():
    ro,col = [int(x) for x in input().split()]

    matrix = [

    ]
    for i in range(ro):
        elements = [x for x in input().split(' ')]
        matrix.append(elements)

    return matrix

matrix = read_matrix()


def is_in(row1,row2,col1,col2,matrix):

    if 0<=row1<len(matrix) or 0<=row2<len(matrix) or 0<=col1<len(matrix[0] or 0<=col2<len(matrix[0])):
        return True

while True:
    args = input().split()
    command = args[0]
    if command == 'END':
        break
    if len(args) != 5:
        print('Invalid input!')
        continue
    row1 = int(args[1])
    col1 = int(args[2])
    row2 = int(args[3])
    col2 = int(args[4])
    my_matrix = matrix

    if command != 'swap':
        print('Invalid input!')
        continue
    if not is_in(row1,row2,col1,col2,matrix):
        print('Invalid input!')
        continue
    else:
        matrix[row1][col1],matrix[row2][col2]=matrix[row2][col2],matrix[row1][col1]
        for num in matrix:
            print(' '.join([str(n) for n in num]))