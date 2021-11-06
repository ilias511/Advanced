number_as_string = input()
nums_dict = {

}
while number_as_string!= 'Search':

    try:
        number_as_int = int(input())
        nums_dict[number_as_string]=number_as_int
    except ValueError:
        print('The variable number must be an integer')

    number_as_string = input()

command = input()

while command!='Remove':
    try:
        print(nums_dict[command])
    except KeyError:
        print('Number does not exists in dictionary')

    command = input()

command = input()
while command!='End':
    try:
        del nums_dict[command]
    except KeyError:
        print('Number does not exists in dictionary')

    command = input()

print(nums_dict)