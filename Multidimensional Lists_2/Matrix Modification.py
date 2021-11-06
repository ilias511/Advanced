def read_matrix():
    ro = int(input())

    matrix = [

    ]

    for i in range(ro):
        elements = [int(x) for x in input().split()]
        matrix.append(elements)

    return matrix

matrix = read_matrix()



def is_in(row1,col1,matrix):

    if 0<=row1<len(matrix) and 0<=col1<len(matrix[0]):
        return True


while True:
    args = input().split()
    command = args[0]
    if command=='END':
        break
    row = int(args[1])
    col = int(args[2])
    value = int(args[3])
    if not is_in(row,col,matrix):
        print('Invalid coordinates')
        continue
    if command=='Add':
        matrix[row][col]+=value
    elif command =='Subtract':
        matrix[row][col]-=value

for m in matrix:
    print(' '.join([str(val) for val in m]))