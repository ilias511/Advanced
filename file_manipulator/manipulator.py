import os

while True:
    command = input()
    if command=='End':
        break
    args = command.split('-')
    file_command = args[0]
    text_file = args[1]
    if file_command =='Create':
        open(text_file,'w').close()
    elif file_command == 'Add':
        write = args[2]
        with open(text_file,'a') as file:
            file.write(write)
            file.write('\n')
    elif file_command =='Replace':
        old_string = args[2]
        new_string = args[3]
        if os.path.exists(text_file):
            with open(text_file,'r+') as file:
                content = file.read().replace(old_string,new_string)
                file.seek(0)
                file.truncate()
                file.write(content)
        else:
            print('An error occurred')
    else:
        if os.path.exists(text_file):
            os.remove(text_file)
        else:
            print('An error occurred')
