
command = input()

nums = [int(x) for x in input().split()]

def odd(numbers):
    values = 0
    for i in numbers:
        if i%2!=0:
            values+=i
    return values * len(numbers)

def even(numbers):
    values = 0
    for i in numbers:
        if i%2==0:
            values+=i
    return values * len(numbers)


if command=='Odd':
    print(odd(nums))
else:
    print(even(nums))