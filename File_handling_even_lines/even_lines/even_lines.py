file = open('text.txt','r')
p = 0
printable = []
for lines in file.readlines():
    if p % 2 == 0:
        printable.append(lines)
    p+=1

changed = []
for i in printable:
    i = i.strip()
    i = i.strip('\'')
    i = i.replace('-','@')
    i = i.replace(',','@')
    i = i.replace('.','@')
    i = i.replace('!','@')
    i = i.replace('?','@')
    i = i.replace("\"""",'')
    changed.append(i)

for line in changed:

    line= ' '.join(line.split()[::-1])
    print(line)
