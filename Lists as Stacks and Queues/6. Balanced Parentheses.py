text = input()
is_valid = True
stack = []
for ch in text:
    if ch in '([{':
        stack.append(ch)
    else:
        if len(stack)==0:
            is_valid=False
            break
        last_opened = stack.pop()
        full_format = f'{last_opened}{ch}'
        if full_format not in '()[]{}':
            is_valid=False
            break
if is_valid:
    print('YES')
else:
    print('NO')

