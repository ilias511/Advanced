points = 0

matrix = []

for i in range(6):
    matrix.append(input().split())

def is_in(r,c,field):
    if 0<=r<len(field) and 0<=c<len(field):
        return True


def bucket_points(matrix, current_row, current_col):
    points_getted = 0
    for r in range(len(matrix)):
        if matrix[r][current_col].isdigit():
            points_getted+= int(matrix[r][current_col])
    return points_getted

for throws in range(3):
    throw = input()
    vals = throw[1:-1].split(', ')
    current_row = int(vals[0])
    current_col = int(vals[1])
    if not is_in(current_row,current_col,matrix) or matrix[current_row][current_col].isdigit():
        continue
    elif matrix[current_row][current_col]=='B':
        point =bucket_points(matrix,current_row,current_col)
        points+=point
        matrix[current_row][current_col]= '.'

if points<100:
    print(f"Sorry! You need {100-points} points more to win a prize.")

elif 100<=points<=199:
    print(f"Good job! You scored {points} points, and you've won Football.")
elif 200<=points<=299:
    print(f"Good job! You scored {points} points, and you've won Teddy Bear.")
elif 300<=points:
    print(f"Good job! You scored {points} points, and you've won Lego Construction Set.")