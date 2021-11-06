count = int(input())
elements = set()
for i in range(count):
    element = input().split()
    for j in element:
        elements.add(j)


for el in elements:
    print(el)