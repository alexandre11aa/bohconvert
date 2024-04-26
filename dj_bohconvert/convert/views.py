from django.shortcuts import render

from convert.models import *

from .functions.binario import decimal_para_binario
from .functions.octal import decimal_para_octal
from .functions.hexadecimal import decimal_para_hexadecimal

from django.shortcuts import render

from django.core.cache import cache
from django.db.models import Count

def get_last_conversions():
    # Verifica se o cache existe
    if 'last_conversions' in cache:
        return cache.get('last_conversions')

    # Se não houver cache, busca no banco de dados
    last_conversions = Convert.objects.annotate(count=Count('id')).order_by('-id')[:5]

    # Adiciona ao cache
    cache.set('last_conversions', last_conversions)

    return last_conversions

def conversor(request):
    if request.method == 'POST':

        # Variaveis

        decimal = request.POST.get('numero_decimal')
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

        # Reseta o cache
        last_conversions = get_last_conversions()
        last_conversions = list(last_conversions)
        last_conversions.insert(0, convert)
        last_conversions.pop()
        cache.set('last_conversions', last_conversions)

        # Retorna a página com os valores calculados preenchidos nos campos
        return render(request, 'conversor.html', {
            'decimal': decimal,
            'binario': binario,
            'octal': octal,
            'hexadecimal': hexadecimal,
            'historico': last_conversions
        })

    # Obtem os ultimos valores do banco de dados
    historico = get_last_conversions()

    return render(request, template_name='conversor.html', context={'historico': historico})