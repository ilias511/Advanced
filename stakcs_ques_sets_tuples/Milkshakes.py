from collections import deque

chocolates = [int(x) for x in input().split(', ')]
milk = [int(x) for x in input().split(', ')]

choco_d = deque(chocolates)
milk_d = deque(milk)
milkshakes = 0
while milkshakes!=5:
    if choco_d:
        last_choco = choco_d.pop()
    if milk_d:
        first_milk = milk_d.popleft()
    if last_choco==first_milk:
        milkshakes+=1
        if milkshakes == 5:
            break
    elif last_choco!=first_milk:
        if last_choco <= 0:
            milk_d.appendleft(first_milk)
        elif first_milk<=0:
            choco_d.append(last_choco)
        else:
            milk_d.append(first_milk)
            last_choco-=5
            choco_d.append(last_choco)

    if not milk_d or not choco_d:
        break

if milkshakes==5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')
if choco_d:
    print(f"Chocolate: {', '.join(str(s) for s in choco_d)}")
else:
    print('Chocolate: empty')
if milk_d:
    print(f"Milk: {', '.join(str(s) for s in milk_d)}")
else:
    print('Milk: empty')