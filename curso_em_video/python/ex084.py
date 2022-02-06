lista = []
listinha = []
continuar = 'S'
pessoas = 0
while continuar == 'S':
    nome = input('Nome: ')
    peso = float(input('Peso: '))
    listinha.append(nome)
    listinha.append(peso)
    lista.append(listinha[:])
    listinha.clear()
    if pessoas == 0:
        pesado = peso
        leve = peso
    elif peso > pesado:
        pesado = peso
    elif peso < leve:
        leve = peso
    pessoas += 1
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
print(f'Você cadastrou {pessoas} pessoas.')
print(f'O maior peso foi {pesado} Kg. De ', end='')
for x in lista:
    if x[1] == pesado:
        print(x[0], end=' ')
print(f'\nO menor peso foi {leve} Kg. De ', end='')
for t in lista:
    if t[1] == leve:
        print(t[0], end=' ')

