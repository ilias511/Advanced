def read_matrix():
    ro = int(input())

    matrix = [

    ]
    for i in range(ro):
        elements = [x for x in input().split(' ')]
        matrix.append(elements)

    return matrix

matrix = read_matrix()

def is_in(r,c,matrix):

    if 0<=r<len(matrix) and 0<=c<len(matrix[0]):
        return True

current_row = 0
current_col = 0
for r in range(len(matrix)):
    is_find = False
    for c in range(len(matrix[r])):
        if matrix[r][c] == 'A':
            current_row=r
            current_col=c
            is_find = True
            matrix[current_row][current_col]='*'
            break
    if is_find:
        break

bags = 0

while bags<10:
    command = input()

    if command == 'up':
        current_row-=1

        if not is_in(current_row,current_col,matrix):
            break
        if matrix[current_row][current_col].isdigit():
            bags+=int(matrix[current_row][current_col])
            matrix[current_row][current_col]='*'
        if matrix[current_row][current_col] == 'R':
            matrix[current_row][current_col] = '*'
            break
        else:
            matrix[current_row][current_col] = '*'
    elif command == 'down':
        current_row+=1
        if not is_in(current_row,current_col,matrix):
            break
        if matrix[current_row][current_col].isdigit():
            bags+=int(matrix[current_row][current_col])
            matrix[current_row][current_col]='*'
        if matrix[current_row][current_col] == 'R':
            matrix[current_row][current_col] = '*'
            break
        else:
            matrix[current_row][current_col] = '*'
    elif command == 'right':
        current_col+=1
        if not is_in(current_row,current_col,matrix):
            break
        if matrix[current_row][current_col].isdigit():
            bags+=int(matrix[current_row][current_col])
            matrix[current_row][current_col]='*'
        if matrix[current_row][current_col] == 'R':
            matrix[current_row][current_col] = '*'
            break
        else:
            matrix[current_row][current_col] = '*'
    elif command == 'left':
        current_col-=1
        if not is_in(current_row,current_col,matrix):
            break
        if matrix[current_row][current_col].isdigit():
            bags+=int(matrix[current_row][current_col])
            matrix[current_row][current_col]='*'
        if matrix[current_row][current_col] == 'R':
            matrix[current_row][current_col] = '*'
            break
        else:
            matrix[current_row][current_col] = '*'

if bags>=10:
    print('She did it! She went to the party.')
    for i in matrix:
        print(' '.join([v for v in i]))
else:
    print("Alice didn't make it to the tea party.")
    for i in matrix:
        print(' '.join([v for v in i]))