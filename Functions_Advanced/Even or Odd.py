def even_odd(*args):
    command = args[-1]
    nums = []
    if command=='even':
        for i in args[:-1]:
            if i % 2 == 0:
                nums.append(i)
        return nums
    elif command == 'odd':
        for i in args[:-1]:
            if i % 2 != 0:
                nums.append(i)
        return nums


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))