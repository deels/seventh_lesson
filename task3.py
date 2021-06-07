# TODO: Task 3
#  A simple calculator.
#  Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter (to keep
#  things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers) as the second
#  parameter. Then return the sum or product of all the numbers in the arbitrary parameter.

def make_operation(a, *args):
    result = args[0]
    i = 1
    while i < len(args):
        if '+' in a:
            result += args[i]
            i += 1
        elif '-' in a:
            result -= args[i]
            i += 1
        elif '*' in a:
            result *= args[i]
            i +=1
        else:
            print('Укажите действие над числами на первой позиции.')
    return result

print('Result: ' ,make_operation('+', 7, 7, 2))
print('Result: ', make_operation('-', 5, 5, -10, -20))
print('Result: ', make_operation('*', 7, 6))
