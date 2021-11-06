from collections import deque

values = deque()
stack = []
queries = int(input())

for i in range(queries):
    queries_type = input().split()
    num = queries_type[0]
    if num == '1':
        values.append(int(queries_type[1]))
    elif num == '2':
        if values:
            values.pop()
    elif num == '3':
        if values:
            print(max(values))
    elif num == '4':
        if values:
            print(min(values))


for i in range(len(values)):
    stack.append(values.pop())

print(', '.join([str(f) for f in stack]))
