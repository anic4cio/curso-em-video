def porcentagem_mais(numero, taxa):
    total = numero + (numero * taxa) / 100
    return f'R${total:.2f}'.replace('.', ',')

def porcentagem_menos(numero, taxa):
    total = numero - (numero * taxa) / 100
    return f'R${total:.2f}'.replace('.', ',')

def dobro(numero):
    total = numero * 2
    return f'R${total:.2f}'.replace('.',',')

def triplo(numero):
    total = numero * 3
    return f'R${total:.2f}'.replace('.',',')