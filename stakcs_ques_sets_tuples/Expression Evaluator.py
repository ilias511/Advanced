import math
from collections import deque

string = deque(input().split())

result = 0
nums = deque()
while string:
    character = string.popleft()
    if character.isdigit():
        nums.append(int(character))
    elif character[1:].isdigit():
        nums.append(int(character))

    elif character=='-':
        result = nums.popleft()

        while nums:
            first = nums.popleft()
            result = result - first
        nums.append(result)
    elif character == '*':
        result = nums.popleft()

        while nums:
            first = nums.popleft()
            result = result * first
        nums.append(result)
    elif character == '/':
        result = nums.popleft()

        while nums:
            first = nums.popleft()
            result = result // first
        nums.append(result)
    elif character == '+':
        result = nums.popleft()

        while nums:
            first = nums.popleft()
            result = result + first
        nums.append(result)
print(result)