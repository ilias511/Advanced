
def read_matrix():
    line = int(input())

    matrix = [

    ]
    for i in range(line):
        elements = [int(x) for x in input().split(' ')]
        matrix.append(elements)
    return matrix


my_matrix = read_matrix()

lines = len(my_matrix)
rows = len(my_matrix[0])


primary = []
secondary = []
found = False
for l in range(0,lines):

    present_number = my_matrix[l][l]
    primary.append(present_number)

for x in range(0,lines):
    num = my_matrix[x][lines-x-1]
    secondary.append(num)

#joined_primary =  ', '.join([str(x) for x in primary])
#joined_secondary =  ', '.join([str(x) for x in secondary])
#print(f"Primary diagonal: {joined_primary}. Sum: {sum(primary)}")
#print(f"Secondary diagonal: {joined_secondary}. Sum: {sum(secondary)}")

primary_sum = (sum(primary))
secondary_sum = (sum(secondary))

print(abs(primary_sum-secondary_sum))