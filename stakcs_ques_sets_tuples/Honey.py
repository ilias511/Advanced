from collections import deque

working_bees = deque([int(x) for x in input().split()])
nectar = deque([int(x) for x in input().split()])

symbols = input().split()

honey = 0
while working_bees and nectar:
    first_bee = working_bees.popleft()
    last_nectar = nectar.pop()
    if last_nectar>=first_bee:
        present_symbol = symbols.pop(0)

        if present_symbol == '+':
            honey += abs(first_bee + last_nectar)
        elif present_symbol == '-':
            honey += abs(first_bee - last_nectar)
        elif present_symbol == '*':
            honey += abs(first_bee * last_nectar)
        else:
            if last_nectar>0:
                honey += abs(first_bee / last_nectar)
    else:
        working_bees.appendleft(first_bee)


print(f'Total honey made: {honey}')
if working_bees:
    bee = ', '.join(str(s) for s in working_bees)
    print(f"Bees left: {bee}")
if nectar:
    nec = ', '.join(str(s) for s in nectar)
    print(f"Nectar left: {nec}")