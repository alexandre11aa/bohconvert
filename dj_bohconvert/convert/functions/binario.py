def decimal_para_binario(decimal, precisao=8):

    # Converter vírgula para ponto
    decimal = float(decimal.replace(",", "."))

    # Converter parte inteira para binário
    parte_inteira = bin(int(decimal))[2:]

    # Converter parte fracionária para binário
    parte_fracionaria = ''
    if decimal % 1 != 0:
        parte_fracionaria = '.'
        fracionaria = decimal - int(decimal)
        for _ in range(precisao):
            fracionaria *= 2
            parte_fracionaria += str(int(fracionaria))
            fracionaria -= int(fracionaria)

    return parte_inteira + parte_fracionaria