from collections import  deque




box_material = [int(x) for x in input().split()]
magic_level = deque(int(x) for x in input().split())
presents_magic = {
    150:'Doll',
    250:'Wooden train',
    300:'Teddy bear',
    400: 'Bicycle'
}
presents_magic_values = {}
while box_material and magic_level:

    box_last = box_material.pop()
    magic_first = magic_level.popleft()

    multiplication = box_last * magic_first

    if magic_first == 0 and box_last == 0:
        continue
    if box_last==0:
        magic_level.appendleft(magic_first)
        continue
    if magic_first == 0:
        box_material.append(box_last)
        continue

    if multiplication <0:
        summary = box_last + magic_first
        box_material.append(summary)
    elif multiplication in presents_magic:
        gift = presents_magic[multiplication]
        if gift not in presents_magic_values:
            presents_magic_values[gift]=1
        else:
            presents_magic_values[gift]+=1

    else:

        box_material.append(box_last+15)

is_done = ('Doll'in presents_magic_values.keys() and 'Wooden train' in presents_magic_values.keys()) or ('Teddy bear' in presents_magic_values.keys() and 'Bicycle' in presents_magic_values.keys())
if is_done:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if box_material:
    rvr = reversed(box_material)
    print(f"Materials left: {', '.join([str(s) for s in rvr])}")
if magic_level:
    print(f"Materials left: {', '.join([str(s) for s in magic_level])}")

for key,value in sorted(presents_magic_values.items()):
    print(f'{key}: {value}')
