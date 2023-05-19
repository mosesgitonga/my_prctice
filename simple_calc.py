import sys
print("\t \t Welcome to My Calculator")

def  add():
    arguments = sys.argv
    total = 0
    for i in range(2, len(arguments)):
        total = total + int(arguments[i])
    return total


def sub():
    arguments = sys.argv
    minus = int(arguments[2])
    for i in range (3, len(arguments)):
        minus -= int(arguments[i])
    return minus


def mul():
    arguments = sys.argv
    product = 1
    for i in range(2, len(arguments)):
        product = product * int(arguments[i])
    return product    
def div():
    arguments = sys.argv
    division = int(arguments[2])
    for i in range(3, len(arguments)):
        division /= int(arguments[i])
    return division


def execute():
    arguments = sys.argv
    
    operators = ['+', '-', 'x', '/']
    for sign in operators:
        if sign in arguments:
                if sign == '-':
                    res = sub()
                elif sign == 'x':
                    res = mul()
                elif sign == '+':
                    res = add()
                elif sign == '/':
                    res = div()
                elif sign == 'p':
                    res = power()
                print(res)
                break
    else:
        print("operator not recognized")


execute()
