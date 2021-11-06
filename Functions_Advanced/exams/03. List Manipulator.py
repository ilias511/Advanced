def list_manipulator(lst,command,position,*args):
    if command=='add':
        if position=='beginning':
            if args:
                for i in reversed(args):
                    lst.insert(0,i)
        elif position =='end':
            if args:
                for i in args:
                    lst.append(i)

    elif command=='remove':
        if position=='beginning':
            if not args:
                lst.pop(0)
            elif args:
                num = args[0]
                for i in range(num):
                    lst.remove(lst[0])
        elif position=='end':
            if not args:
                lst.pop()
            elif args:
                num = args[0]
                for i in range(num):
                    lst.pop()
    return lst

print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))