numbers = input().split()

first_num = int(numbers[0])
second_num = int(numbers[1])

set_num_one = set()
set_num_two = set()
for n in range(first_num):
    set_num_one.add(int(input()))

for m in range(second_num):
    set_num_two.add(int(input()))



same_nums = set_num_one & set_num_two

for k in same_nums:
    print(k)