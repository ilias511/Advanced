from collections import deque


bomb_effect = deque(int(x) for x in input().split(', '))
bomb_casing = deque(int(x) for x in input().split(', '))

datura = 0
cherry = 0
smoke_decoy = 0
succeeded = False

while bomb_casing and bomb_effect:
    if datura>=3 and cherry>=3 and smoke_decoy>=3:
        succeeded = True
        break
    else:
        b_effect =int(bomb_effect.popleft())
        b_case = int(bomb_casing.pop())
        value = b_case+b_effect

        if value==40:
            datura+=1
        elif value == 60:
            cherry+=1
        elif value == 120:
            smoke_decoy+=1
        else:
            bomb_casing.append(b_case-5)
            bomb_effect.appendleft(b_effect)

if not succeeded:
    print("You don't have enough materials to fill the bomb pouch.")
    if not bomb_effect:
        print('Bomb Effects: empty')
    else:
        print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effect])}")
    if not bomb_casing:
        print('Bomb Casings: empty')
    else:
        print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casing])}")

if succeeded:
    print("Bene! You have successfully filled the bomb pouch!")
    if not bomb_effect:
        print('Bomb Effects: empty')
    else:
        print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effect])}")
    if not bomb_casing:
        print('Bomb Casings: empty')
    else:
        print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casing])}")

print(f'Cherry Bombs: {cherry}')
print(f'Datura Bombs: {datura}')
print(f'Smoke Decoy Bombs: {smoke_decoy}')