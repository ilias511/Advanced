


def numbers_searching(*args):
    duplicate = []
    for i in range(1,len(args)-2):
        if args.count(args[i])>1:
            duplicate.append(args[i])
    duplicate = sorted(list(set(duplicate)))
    missing_num = [x for x in range(duplicate[0], duplicate[-1]+1) if x not in duplicate]
    return [missing_num[0],duplicate]

print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))