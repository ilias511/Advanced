from collections import deque

quantity_food = int(input())


orders_not_completed = False
maxi = 0

orders = input().split(' ')
quantity_of_the_order = deque(orders)
for i in (orders):
    if int(i)>maxi:
        maxi =int(i)

    if quantity_food>=int(i):
        quantity_food-=int(i)
        quantity_of_the_order.popleft()
    else:
        orders_not_completed = True
        break

if orders_not_completed:
    print(maxi)
    print(f"Orders left: {' '.join(quantity_of_the_order)}")
else:
    print(maxi)
    print('Orders complete')