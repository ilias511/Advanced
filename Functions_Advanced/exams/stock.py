def stock_availability(*args):
    list_of_flavors = args[0]
    command = args[1]

    if command == 'delivery':
        boxes = args[2:]
        for v in boxes:
            list_of_flavors.append(v)
        return list_of_flavors
    elif command == 'sell':
        values = args[2:]
        if len(values) == 0:
            list_of_flavors.pop(0)
        elif type(values[0])==int:
            for b in range(int(values[0])):
                list_of_flavors.pop(0)
        else:
            for val in values:
                while val in list_of_flavors:
                    list_of_flavors.remove(val)

    return list_of_flavors


print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
