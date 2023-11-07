
def calculation(n1,n2,op):
    if op == '+':
        result = n1+n2
    elif op == '-':
        result = n1-n2
    elif op == '*':
        result = n1*n2
    elif op == '/':
        result = n1/n2
    elif op == '^':
        result = n1**n2
    else:
        result = "Invalid operator"

    return result

number1 = float(input('Value 1'))
op = input('Enter operator (+,-,*,/,^):')
number2 = float(input('Value 2'))
print(number1, op, number2)
result=calculation(number1,number2,op)
print(number1, op, number2,'=', result)