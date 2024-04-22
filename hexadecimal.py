def decimal_para_hexadecimal(decimal, precisao=8):
    parte_inteira = hex(int(decimal))[2:]  # Converter parte inteira para hexadecimal
    parte_fracionaria = ''

    # Converter parte fracionária para hexadecimal
    if decimal % 1 != 0:
        parte_fracionaria = '.'
        fracionaria = decimal - int(decimal)
        for _ in range(precisao):
            fracionaria *= 16
            parte_fracionaria += str(hex(int(fracionaria)))[2:]
            fracionaria -= int(fracionaria)

    return parte_inteira + parte_fracionaria

# Exemplo de uso
decimal_fracionario = 428.625
hexadecimal = decimal_para_hexadecimal(decimal_fracionario)
print(f'O número decimal fracionário {decimal_fracionario} em hexadecimal é: {hexadecimal}')