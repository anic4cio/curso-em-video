def porcentagem_mais(numero, maior, format=True):
    total = numero + (numero * maior) / 100
    if format:
        return f'R${total:.2f}'.replace('.', ',')
    else:
        return total

def porcentagem_menos(numero, taxa, format=True):
    total = numero - (numero * taxa) / 100
    if format:
        return f'R${total:.2f}'.replace('.', ',')
    else:
        return total

def dobro(numero, format=True):
    total = numero * 2
    if format:
        return f'R${total:.2f}'.replace('.',',')
    else:
        return total

def triplo(numero, format=True):
    total = numero * 3
    if format:
        return f'R${total:.2f}'.replace('.',',')
    else:
        return total

def resumo(numero=0, maior=10, menor=10):
    print('~' * 30)
    print(f'{"Resumo do Valor":^30}')
    print('~' * 30)
    print(f'Dobro de R${numero}: {dobro(numero)}')
    print(f'Triplo de R${numero}: {triplo(numero)}')
    print(f'R${numero} mais {maior}%: {porcentagem_mais(numero, maior)}')
    print(f'R${numero} menos {menor}%: {porcentagem_menos(numero, menor)}')