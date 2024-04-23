from django.shortcuts import render

from convert.models import *

from .functions.binario import decimal_para_binario
from .functions.octal import decimal_para_octal
from .functions.hexadecimal import decimal_para_hexadecimal

# views.py
from django.shortcuts import render
from django.http import HttpResponse

def conversor(request):
    if request.method == 'POST':

        # Variaveis

        decimal = float(request.POST.get('numero_decimal'))
        precisao = int(request.POST.get('precisao').split()[0])
        binario = decimal_para_binario(decimal, precisao)
        octal = decimal_para_octal(decimal, precisao)
        hexadecimal = decimal_para_hexadecimal(decimal, precisao)

        # Armazenamento

        convert = Convert.objects.create(
            decimal=decimal,
            precisao=precisao,
            binario=binario,
            octal=octal,
            hexadecimal=hexadecimal
        )

        # Validacao

        return HttpResponse(f'D: {decimal}, B: {binario}, O: {octal}, H: {hexadecimal}, P: {precisao}')

    return render(request, template_name='conversor.html')
