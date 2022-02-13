"""
Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
#Essa função funciona perfeitamente se chamá-la sem passar parâmetros; "maior()"
def maior(* numeros):
    total = len(numeros)
    if len(numeros) > 0:
        print(f'Foram passados {total} valores e o maior número foi {max(numeros)}')
    else:
        print('Nenhum valor informado!')        


#Já essa função, não funciona se chamar sem passar nenhum parâmetro; "maior()"
def maior(* numeros):
    maior = max(numeros)
    total = len(numeros)
    if len(numeros) > 0:
        print(f'Foram passados {total} valores e o maior número foi {maior}')
    else:
        print('Nenhum valor informado!')


maior(9, 2, 11, 5, 3)
maior(4, 7, 1, 2)
maior(1, 2, 3, 7, 3, 9, 5, 12)
maior(6)
maior(1, 2)

#O maior mistério da humanidade
maior()
