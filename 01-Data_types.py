def datatypes(datatype, value):
    if datatype == 'int':
        result = 2 * int(value)
    elif datatype == 'real':
        result = f'{1.5 * float(value):.2f}'
    elif datatype == 'string':
        result = f'${value}$'
    return result


datatype, value = input(), input()
print(datatypes(datatype, value))
