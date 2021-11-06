def flights(*args):
    info_dict = {}
    i = 0

    while i<len(args):
        if args[i] == 'Finish':
            break
        elif args[i] not in info_dict:
            info_dict[args[i]]=args[i+1]
            i += 2
        else:
            info_dict[args[i]]+=args[i+1]
            i += 2

    return info_dict

print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))