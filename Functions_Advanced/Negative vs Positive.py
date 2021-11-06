def positive(number):
    value = 0
    for i in number:
        if i > 0:
            value += i
    return value

def negatives(number):
    value = 0
    for i in number:
        if i<0:
            value+=i
    return value

numbers = [int(i) for i in input().split()]


print(negatives(numbers))
print(positive(numbers))

if positive(numbers)>abs(negatives(numbers)):
    print('The positives are stronger than the negatives')
else:
    print('The negatives are stronger than the positives')
