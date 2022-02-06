lista = []
continuar = '1'
while continuar == '1':
    numero = int(input('Digite um número: '))
    lista.append(numero)
    continuar = input('[1] para continuar ou [0] para parar: ')
print(f'Ao todo foram digitados {len(lista)} valores.')
lista.sort(reverse=True)
print(f'A ordem decrescente dos itens da lista é {lista}.')
if 5 in lista:
    print(f'O primeiro número 5 está na posição {lista.index(5)+1} da lista')
else:
    print('O número 5 não está na lista!')


