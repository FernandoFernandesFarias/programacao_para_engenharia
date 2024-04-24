def decimal_para_binario(decimal):
    if decimal == 0:
        return '0'
    binario = ''
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return binario

def decimal_para_octal(decimal):
    if decimal == 0:
        return '0'
    octal = ''
    while decimal > 0:
        octal = str(decimal % 8) + octal
        decimal = decimal // 8
    return octal

def decimal_para_hexadecimal(decimal):
    if decimal == 0:
        return '0'
    hexadecimal = ''
    while decimal > 0:
        resto = decimal % 16
        if resto < 10:
            hexadecimal = str(resto) + hexadecimal
        else:
            hexadecimal = chr(65 + resto - 10) + hexadecimal
        decimal = decimal // 16
    return hexadecimal

numero_decimal = int(input("Digite um número decimal: "))
binario = decimal_para_binario(numero_decimal)
octal = decimal_para_octal(numero_decimal)
hexadecimal = decimal_para_hexadecimal(numero_decimal)

print("O número decimal", numero_decimal, "em binário é:", binario)
print("O número decimal", numero_decimal, "em octal é:", octal)
print("O número decimal", numero_decimal, "em hexadecimal é:", hexadecimal)
