lista = []
continuar = 'S'
while continuar == 'S':
    numero = int(input('Digite um número: '))
    if numero in lista:
        print('Este número já está na lista.')
    else:
        lista.append(numero)
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
print(f'Os números da lista foram: {sorted(lista)}')
