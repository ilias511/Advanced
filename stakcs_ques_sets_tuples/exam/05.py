from collections import deque

order_pizza = deque([int(x) for x in input().split(', ')])
employees = deque([int(x) for x in input().split(', ')])

orders_completed = False
pizzas = 0
while employees:
    if not order_pizza:
        orders_completed= True
        break
    first_order = order_pizza.popleft()
    if first_order<=0:
        continue
    elif first_order>10:
        continue
    employee_task = employees.pop()
    if first_order<=employee_task:
        pizzas+=first_order
    elif first_order>employee_task:
        first_order-=employee_task
        pizzas+=employee_task
        order_pizza.appendleft(first_order)

if orders_completed:
    print(f"All orders are successfully completed!")
    print(f"Total pizzas made: {pizzas}")
    if employees:
        print(f"Employees: {', '.join([str(x) for x in employees])}")
else:
    print('Not all orders are completed.')
    if order_pizza:
        print(f"Orders left: {', '.join([str(x) for x in order_pizza])}")