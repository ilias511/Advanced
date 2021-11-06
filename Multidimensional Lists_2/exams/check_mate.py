
moves = {
    'up':(-1,0),
    'down':(1,0),
    'left':(0,-1),
    'right':(0,1),
    'up-right':(-1,1),
    'up-left':(-1,-1),
    'down-left':(1,-1),
    'down-right':(1,1)
}
def is_in(r,c,field):
    if 0<=r<len(field) and 0<=c<len(field):
        return True
board = [input().split(' ') for i in range(8)]
checks = []
for r in range(len(board)):
    for c in range(len(board[0])):
        if board[r][c]=='Q':
            for val in moves:
                r_move = moves[val][0]
                c_move = moves[val][1]
                r_moves = r+r_move
                c_moves = c+c_move
                while is_in(r_moves,c_moves,board):
                    if board[r_moves][c_moves]=='Q':
                        break
                    elif board[r_moves][c_moves]=='K':
                        checks.append([r,c])
                        break
                    r_moves+=r_move
                    c_moves+=c_move
if checks:
    for c in checks:
        print(c)
else:
    print('The king is safe!')