from collections import deque


materials_for_wedding = deque([int(x) for x in input().split()])
genie_magic_level = deque([int(x) for x in input().split()])

materials= {'Gemstone': 0,
            'Porcelain Sculpture': 0,
            'Gold':0,
            'Diamond Jewellery':0}


succeeded = False


while materials_for_wedding and genie_magic_level:
    material = materials_for_wedding.pop()
    magic_level = genie_magic_level.popleft()
    summary = material+magic_level
    if summary<100:
        if summary%2==0:
            material = material *2
            magic_level = magic_level*3
            summary = material + magic_level
        else:
            summary*=2
    elif summary>499:
        material/=2
        magic_level/=2
        summary = material + magic_level

    if 100 <= summary <= 199:
        materials['Gemstone'] += 1
    elif 200 <= summary <= 299:
        materials['Porcelain Sculpture'] += 1
    elif 300 <= summary <= 399:
        materials['Gold'] += 1
    elif 400 <= summary <= 499:
        materials['Diamond Jewellery'] += 1
    else:
        continue

if materials['Gemstone']>0 and materials['Porcelain Sculpture']>0 or materials['Gold']>0 and materials['Diamond Jewellery']>0:
    succeeded = True

if succeeded:
    print('The wedding presents are made!')
else:
    print('Aladdin does not have enough wedding presents.')
if materials_for_wedding:
    print(f"Materials left: {', '.join([str(x) for x in materials_for_wedding])}")
if genie_magic_level:
    print(f"Magic left: {', '.join([str(x) for x in genie_magic_level])}")

for key,value in sorted(materials.items(), key=lambda x: x[0]):
    if value>0:
        print(f'{key}: {value}')
