def porcentagem_mais(numero, taxa, format=True):
    total = numero + (numero * taxa) / 100
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
