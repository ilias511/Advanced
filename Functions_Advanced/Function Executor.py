def func_executor(command):
    n1,n2 = command[1]
    value = command[0]
    args = value(n1,n2)
    return [args]


def sum_numbers(num1, num2):
    return num1+num2

def multiply_numbers(num1, num2):
    return num1 * num2
print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))