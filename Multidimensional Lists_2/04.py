def is_in(r,c,size):

    if 0<=r<size and 0<=c<size:
        return True

size = int(input())
matrix = []

bunny_row = 0
bunny_col = 0
for row in range(size):
    elements = input().split()
    matrix.append(elements)
    for col in range(size):
        element = elements[col]
        if element == 'B':
            bunny_row,bunny_col = row,col


#for r in range(len(matrix)):
 #   is_find = False
  #  for c in range(len(matrix[r])):
   #     if matrix[r][c] == 'B':
    #        bunny_row=r
     #       bunny_col=c
      #      is_find = True
       #     break
    #if is_find:
     #   break


moving = {
    'right': lambda r,c:(r,c+1),
    'left': lambda r,c:(r,c-1),
    'up': lambda r,c:(r-1,c),
    'down': lambda r,c:(r+1,c)
}

best_direction = ''
most_points = float('-inf')
best_list_directions = []
for direction,step in moving.items():
    current_row = bunny_row
    current_col = bunny_col
    points = 0
    values = []
    while True:
        current_row,current_col= step(current_row,current_col)
        if not is_in(current_row,current_col,size):
            break
        if matrix[current_row][current_col] == 'X':
            break
        points+=int(matrix[current_row][current_col])
        values.append([current_row,current_col])
    if points>most_points:
        most_points=points
        best_direction = direction
        best_list_directions = values


print(best_direction)
for i in best_list_directions:
    print(i)
print(most_points)