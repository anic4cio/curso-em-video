#Só funciona com 4 digitos
# num = input('Digite um número qualquer: ')
# uni = (num[~0])
# dez = (num[~1])
# cent = (num[~2])
# mil = (num[~3])
# print('Unidades: {}'.format(uni))
# print('Dezenas: {}'.format(dez))
# print('Centenas: {}'.format(cent))
# print('Milhar: {}'.format(mil))

num = int(input('Digite o número: '))
dez = num // 10 % 10
print('Dezena: {}'.format(dez))

"""
Veja os exemplos abaixo.
Divisão: 1234 / 10 = 123,4
Divisão inteira: 1234 //10 = 123
Módulo: 1234 % 10 = 4
Pra ele descobrir a centena ele faz isso:
Faz a divisão inteira por 100: 1234 // 100 = 12
Depois pega o resultado e dividi por 10, mas pega só o resto dessa divisão (que é o módulo): 12 % 10 = 2
Ou seja, a centena é 2.
"""

#No dia seguinte
num = int(input('Digite um número de 0 a 9999: '))
uni = num % 10
dez = num // 10 % 10
cent = num // 100 % 10
mil = num // 1000 % 10
print('Unidades: {}'.format(uni))
print('Dezenas: {}'.format(dez))
print('Centenas: {}'.format(cent))
print('Milhares: {}'.format(mil))
