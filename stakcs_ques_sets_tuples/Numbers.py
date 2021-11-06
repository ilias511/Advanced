seq_num_one = set()
seq_num_two = set()


num1 = input().split()
num2 = input().split()

for i in num1:
    seq_num_one.add(int(i))

for j in num2:
    seq_num_two.add(int(j))

iterations = int(input())


for it in range(iterations):
    command = input().split()
    move = command[0]
    seq = command[1]
    command.remove(move)
    command.remove(seq)
    if move=='Add' and seq == 'First':
        for m in command:
            seq_num_one.add(int(m))
    elif move == 'Add' and seq == 'Second':
        for m in command:
            seq_num_two.add(int(m))
    elif move=='Remove' and seq == 'Second':
        for m in command:
            if int(m) in seq_num_two:
                seq_num_two.remove(int(m))
    elif move=='Remove' and seq == 'First':
        for m in command:
            if int(m) in seq_num_one:
                seq_num_one.remove(int(m))
    elif move == 'Check' and seq =='Subset':
        if seq_num_one.issubset(seq_num_two) or seq_num_two.issubset(seq_num_one):
            print(True)
        else:
            print(False)
if seq_num_one:
    srt = sorted(seq_num_one)
    print(', '.join(str(s) for s in srt))
if seq_num_two:
    srt = sorted(seq_num_two)
    print(', '.join(str(s) for s in srt))
