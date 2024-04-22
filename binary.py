def decimal_para_binario(decimal, precisao=8):
    parte_inteira = bin(int(decimal))[2:]  # Converter parte inteira para binário
    parte_fracionaria = ''

    # Converter parte fracionária para binário
    if decimal % 1 != 0:
        parte_fracionaria = '.'
        fracionaria = decimal - int(decimal)
        for _ in range(precisao):
            fracionaria *= 2
            parte_fracionaria += str(int(fracionaria))
            fracionaria -= int(fracionaria)

    return parte_inteira + parte_fracionaria

# Exemplo de uso
decimal_fracionario = 428.625
binario = decimal_para_binario(decimal_fracionario)
print(f'O número decimal fracionário {decimal_fracionario} em binário é: {binario}')