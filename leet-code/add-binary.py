def binaryToDecimal(a):
    sum = 0
    i = 0
    while i < len(a):
        sum = sum + int(a[i]) * pow(2, len(a) - 1 - i)
        i += 1

    return sum

def decimalToBinary(num): 
    if num > 1: 
        decimalToBinary(num // 2) 
    return num % 2

def addBinary(a, b) -> str:
    a_decimal = binaryToDecimal(a)
    b_decimal = binaryToDecimal(b)

    return decimalToBinary(a_decimal + b_decimal)


print(addBinary("11", "1"))