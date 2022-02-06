valores = tuple(int(input('Digites o número: ')) for c in range(1, 5))
print(f'Você digitou os valores: {valores}')
print(f'O número 9 apareceu {valores.count(9)} vezes.')
if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3)+1} posição.')
else:
    print('O número 3 não apareceu em nenhuma posição.')
print(f'Valores pares: ', end='')
for valor in valores:
    if valor % 2 == 0:
        print(valor, end=' ')