names_count = int(input())

names = set()
for i in range(names_count):
    name_given = input()
    names.add(name_given)


for j in names:
    print(j)