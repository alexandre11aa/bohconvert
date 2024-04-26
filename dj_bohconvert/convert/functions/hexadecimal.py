def decimal_para_hexadecimal(decimal, precisao=8):

    # Converter vírgula para ponto
    decimal = float(decimal.replace(",", "."))

    # Converter parte inteira para hexadecimal
    parte_inteira = hex(int(decimal))[2:]

    # Converter parte fracionária para hexadecimal
    parte_fracionaria = ''
    if decimal % 1 != 0:
        parte_fracionaria = '.'
        fracionaria = decimal - int(decimal)
        for _ in range(precisao):
            fracionaria *= 16
            parte_fracionaria += str(hex(int(fracionaria)))[2:]
            fracionaria -= int(fracionaria)

    return parte_inteira + parte_fracionaria