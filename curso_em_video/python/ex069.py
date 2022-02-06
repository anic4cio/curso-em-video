pessoas = mais_18 = homens = mulher_20 = 0
while True:
    continuar = ' '
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo: [M/F] ')).upper().strip()[0]
    if idade > 18:
        mais_18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher_20 += 1
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        print('Programa encerrado!')
        break
print(f'Pessoas maiores de idade: {mais_18}')
print(f'Total de homens: {homens}')
print(f'Total de mulheres abaixo dos 20: {mulher_20}')
