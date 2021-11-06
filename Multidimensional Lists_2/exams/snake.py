def find_player(matrix):
    r,c = 0,0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col]=='S':
                r,c = row,col
                return r, c


def find_next_burrows(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 'B':
                return row, col


size = int(input())
field = [list(input()) for _ in range(size)]
snake_r,snake_c = find_player(field)


def is_in(r,c,field):
    if 0<=r<len(field) and 0<=c<len(field):
        return True

def up_move(r,c,matrix):
    matrix[r][c]='.'
    if not is_in(r-1,c,matrix):
        return False
    next_pos = matrix[r-1][c]
    if next_pos == '*':
        return r - 1, c
    elif next_pos=='B':
        matrix[r-1][c] = '.'
        next_b_r, next_b_c = find_next_burrows(field)
        return next_b_r, next_b_c

    return r-1,c


def down_move(r,c,matrix):
    matrix[r][c] = '.'
    if not is_in(r + 1, c, matrix):
        return False
    next_pos = matrix[r + 1][c]
    if next_pos == '*':
        return r + 1, c
    elif next_pos=='B':
        matrix[r+1][c] = '.'
        next_b_r, next_b_c = find_next_burrows(field)
        return next_b_r, next_b_c

    return r + 1, c

is_out = False


def left_move(r, c, matrix):
    matrix[r][c] = '.'
    if not is_in(r, c-1, matrix):
        return False
    next_pos = matrix[r][c-1]
    if next_pos == '*':
        return r, c - 1
    elif next_pos=='B':
        matrix[r][c-1] ='.'
        next_b_r,next_b_c = find_next_burrows(field)
        return next_b_r,next_b_c

    return r, c-1
def right_move(r, c, matrix):
    matrix[r][c] = '.'
    if not is_in(r, c+1, matrix):
        return False
    next_pos = matrix[r][c+1]
    if next_pos == '*':
        return r, c + 1
    elif next_pos=='B':
        matrix[r][c + 1] = '.'
        next_b_r, next_b_c = find_next_burrows(field)
        return next_b_r, next_b_c

    return r, c+1

enough_food = False
food = 0
while True:

    command = input()
    if command=='up':
        new_moves = up_move(snake_r,snake_c,field)
        if new_moves == False:
            is_out = True
            break
        snake_r, snake_c= new_moves
        if field[snake_r][snake_c] == 'B':
            field[snake_r][snake_c] = 'S'
        elif field[snake_r][snake_c]=='*':
            food += 1
            field[snake_r][snake_c] = 'S'
        else:
            field[snake_r][snake_c] = 'S'
    elif command=='down':
        new_moves = down_move(snake_r,snake_c,field)

        if new_moves == False:
            is_out = True
            break
        snake_r, snake_c = new_moves
        if field[snake_r][snake_c] == 'B':
            field[snake_r][snake_c] = 'S'
        elif field[snake_r][snake_c] == '*':
            food += 1
            field[snake_r][snake_c] = 'S'
        else:
            field[snake_r][snake_c] = 'S'
    elif command=='left':
        new_moves = left_move(snake_r,snake_c,field)

        if new_moves == False:
            is_out = True
            break
        snake_r, snake_c = new_moves
        if field[snake_r][snake_c]=='B':
            field[snake_r][snake_c]='S'
        elif field[snake_r][snake_c] == '*':
            food += 1
            field[snake_r][snake_c]='S'
        else:
            field[snake_r][snake_c] = 'S'
    elif command=='right':
        new_moves = right_move(snake_r, snake_c, field)
        if new_moves == False:
            is_out = True
            break
        snake_r, snake_c = new_moves
        if field[snake_r][snake_c] == 'B':
            field[snake_r][snake_c] = 'S'
        elif field[snake_r][snake_c] == '*':
            food += 1
            field[snake_r][snake_c] = 'S'
        else:
            field[snake_r][snake_c] = 'S'
    if food == 10:
        enough_food = True
        break

if enough_food and not is_out:
    print('You won! You fed the snake.')
    print(f'Food eaten: {food}')
    for i in field:
        print(''.join(i))

elif is_out:
    print('Game over!')
    print(f'Food eaten: {food}')
    for i in field:
        print(''.join(i))