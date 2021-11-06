import math


def field_matrix(row):
    matrix = []
    for i in range(row):
        matrix.append(input().split(' '))
    return matrix
def findplayer(matrix):
    r,c = 0,0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col]=='P':
                r,c = row,col
                break
    return r,c
field_row = int(input())
field = field_matrix(field_row)
player_row,player_col = findplayer(field)

coins = 0
path = []
wall_lost = False


new_row,new_col = None,None


def is_in(r,c,field):
    if 0<=r<len(field) and 0<=c<len(field):
        return True


while True:
    commands = input()
    if commands=='up':
        new_row,new_col  = player_row-1,player_col
    elif commands == 'down':
        new_row,new_col  = player_row+1,player_col
    elif commands=='right':
        new_row, new_col = player_row,player_col+1
    elif commands=='left':
        new_row,new_col = player_row,player_col-1
    else:
        pass

    if not is_in(new_row,new_col,field):
        wall_lost = True
        break
    if field[new_row][new_col].isdigit():
        coins+=int(field[new_row][new_col])
        path.append([new_row,new_col])
        if coins>=100:
            break
    elif field[new_row][new_col]=='X':
        wall_lost = True
        break
    player_row,player_col = new_row, new_col

if wall_lost:
    coins = coins - coins*0.5
    coins = math.floor(coins)
    print(f"Game over! You've collected {coins} coins.")
    print('Your path:')
    for i in path:
        print(i)
else:
    print(f"You won! You've collected {coins} coins.")
    print('Your path:')
    for i in path:
        print(i)