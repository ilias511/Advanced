from collections import deque

pumps = int(input())

tours = deque()

for i in range(pumps):
    pump = [int(j) for j in input().split()]
    tours.append(pump)

for attempt in range(pumps):
    car_fuel = 0
    completed = True
    for petrol,distance in tours:
        car_fuel+=petrol
        if distance>car_fuel:
            completed=False
            break
        car_fuel-=distance
    if completed:
        print(attempt)
        break
    else:
        tours.append(tours.popleft())