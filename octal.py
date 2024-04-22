def decimal_para_octal(decimal, precisao=8):
    parte_inteira = oct(int(decimal))[2:]  # Converter parte inteira para octal
    parte_fracionaria = ''

    # Converter parte fracionária para octal
    if decimal % 1 != 0:
        parte_fracionaria = '.'
        fracionaria = decimal - int(decimal)
        for _ in range(precisao):
            fracionaria *= 8
            parte_fracionaria += str(int(fracionaria))
            fracionaria -= int(fracionaria)

    return parte_inteira + parte_fracionaria

# Exemplo de uso
decimal_fracionario = 428.625
octal = decimal_para_octal(decimal_fracionario)
print(f'O número decimal fracionário {decimal_fracionario} em octal é: {octal}')