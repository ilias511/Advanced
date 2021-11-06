clothes_in_the_box = input().split(' ')
clothes_in_the_box_integer = [int(i) for i in clothes_in_the_box]


capacity_for_one_rack = int(input())

racks_used = 1
new_rack = capacity_for_one_rack
while clothes_in_the_box_integer:
    if clothes_in_the_box_integer[-1]<=capacity_for_one_rack:
        capacity_for_one_rack-=clothes_in_the_box_integer[-1]
        clothes_in_the_box_integer.pop()
    else:
        capacity_for_one_rack = new_rack
        racks_used+=1

print(racks_used)