"""
Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos
e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.
"""

lista = []
for i in range(0, 5):
    valor = int(input('Digite um número: '))
    if i == 0 or valor >= lista[len(lista)-1]:
        lista.append(valor)
        print('Adicionado ao final da lista.')
    else:
        for x in range(0, 5):
            if valor < lista[x]:
                lista.insert(x, valor)
                print(f'Adicionado na posição {x} da lista')
                break
print(lista)
