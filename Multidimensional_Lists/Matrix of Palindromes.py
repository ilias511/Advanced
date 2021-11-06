r,c = [int(x) for x in input().split()]

for rows in range(r):
    for columns in range(c):
        print(f'{chr(97+rows)}{chr(97+columns+rows)}{chr(97+rows)}',end=' ')
    print()