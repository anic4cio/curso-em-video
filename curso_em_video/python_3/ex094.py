"""
Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, 
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média
"""

cadastro = {}
lista = []
mulheres = []
pessoas = media = 0
while True:
    cadastro['nome'] = str(input('Nome: '))
    sexo = str(input('Sexo: ')).upper().strip()[0]
    while sexo not in 'FM':
        sexo = str(input('Erro. Responda somente com F ou M: ')).upper().strip()[0]
        if sexo in 'FM':
            continue
    idade = int(input('Idade: '))
    media += idade
    cadastro['sexo'] = sexo
    if sexo == 'F':
        mulheres.append(cadastro["nome"])   
    cadastro['idade'] = idade
    lista.append(cadastro.copy())
    pessoas += 1
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]   
    while continuar not in 'SN':
        continuar = str(input('Erro. Responda com S ou N: ')).strip().upper()[0]
    if continuar == 'N':
        break
media = media / pessoas
print(f'No total, {pessoas} pessoas foram cadastradas')
print(f'A média de idade foi {media:.1f} anos')
print(f'Lista com todas as mulheres: {mulheres}')
print(f'Pessoas com idade acima da média: ')
for x in lista:
    if x['idade'] > int(media):
        print(f' -{x["nome"]} com {x["idade"]} anos de idade.')