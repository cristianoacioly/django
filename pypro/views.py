from django.http import HttpResponse

def cliente (request):
    return HttpResponse('suele acioly beleza e estetica')

def articles(request, year):
    return HttpResponse('o ano enviado foi ' + str(year))

def lerDoBanco(name):
    lista_nomes = [
        {'nome': 'suelle', 'idade': 38},
        {'nome': 'pedro', 'idade': 11},
        {'nome': 'fagner', 'idade': 20},
    ]

    for pessoa in lista_nomes:
        if pessoa['nome'] == 'nome':
            return pessoa
    else:
        return {'nome': 'Nao encontrada', 'idade': 0}

def fname(request, nome):
    result = lerDoBanco(nome)
    if result['idade'] > 0:
        return HttpResponse('A pessoa foi encontrada, ela tem ' + str[result['idade']] + 'anos')
    else:
        return HttpResponse('pessoa nao encontrada')