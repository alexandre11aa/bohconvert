def decimal_para_octal(decimal, precisao=8):

    # Converter parte inteira para octal
    parte_inteira = oct(int(decimal))[2:]
    
    # Converter parte fracionária para octal
    parte_fracionaria = ''
    if decimal % 1 != 0:
        parte_fracionaria = '.'
        fracionaria = decimal - int(decimal)
        for _ in range(precisao):
            fracionaria *= 8
            parte_fracionaria += str(int(fracionaria))
            fracionaria -= int(fracionaria)

    return parte_inteira + parte_fracionaria