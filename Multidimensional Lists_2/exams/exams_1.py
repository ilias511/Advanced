players = input().split(', ')
player_one = players[0]
player_two = players[1]
def read_matrix():

    matrix = [

    ]
    for i in range(7):
        elements = [x for x in input().split(' ')]
        matrix.append(elements)

    return matrix


def is_in(r,matrix):

    if 0<=r<len(matrix):
        return True

def double_deducted(current_row, current_col, matrix):
    up = int(matrix[0][current_col])
    down = int(matrix[6][current_col])
    right = int(matrix[current_row][6])
    left = int(matrix[current_row][0])

    return (up+down+right+left)*2

def triple_deducted(current_row, current_col, matrix):
    up = int(matrix[0][current_col])
    down = int(matrix[6][current_col])
    right = int(matrix[current_row][6])
    left = int(matrix[current_row][0])

    return (up + down + right + left) * 3



matrix = read_matrix()
players_score = {player_one:501,player_two:501}
players_turns = {player_one:0,player_two:0}


i =1
current_player = players[0]
other_player = players[1]
while True:
    pos= input()
    current_row = int(pos[1])
    current_col = int(pos[4])
    if not is_in(current_row,matrix) or not is_in(current_col,matrix):
        players_turns[current_player] += 1
        continue
    elif matrix[current_row][current_col].isdigit():
        players_score[current_player]-=int(matrix[current_row][current_col])

    elif matrix[current_row][current_col]=='D':
        points_deducted = double_deducted(current_row,current_col,matrix)
        players_score[current_player]-=points_deducted

    elif matrix[current_row][current_col]=='T':
        triple_points_deducted = triple_deducted(current_row,current_col,matrix)
        players_score[current_player]-=triple_points_deducted
    elif matrix[current_row][current_col] == 'B':
        players_turns[current_player]+=1
        break
    if players_score[current_player] <= 0:
        players_turns[current_player] += 1
        break
    players_turns[current_player] += 1
    current_player,other_player=other_player,current_player
print(f'{current_player} won the game with {players_turns[current_player]} throws!')
