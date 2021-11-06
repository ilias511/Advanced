def plus(n1,n2):
    return n1 + n2
def multi(n1,n2):
    return n1*n2


def abstract(n1,n2):
    return n1-n2

def divine(n1,n2):
    if n2<0:
        print('Must be greater than 0')
    else:
        return n1/n2

summary = int(input())
symbol = input()


while symbol!='=':

    num2 = int(input())
    if symbol == '+':
        summary+=plus(summary,num2)
    elif symbol == '-':
        summary-= abstract(summary,num2)
    elif symbol =='*':
        summary*=multi(summary,num2)

    elif symbol =='/':
        summary/=divine(summary,num2)
    symbol = input()

print(summary)