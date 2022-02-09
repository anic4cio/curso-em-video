"""
Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
"""

#Eu não sabia o que era progressão aritmética, então minha resolução ficou um pouco diferente
#Código sem ententer o que é PA
ciclo = 0
primeiro = int(input('Digite o primeiro número: '))
final = int(input('Digite o último número: '))
razao = int(input('Digite a razão da progressão aritmetica: '))
for numero in range(primeiro, final, razao):
    print(numero)
    ciclo += 1
    if ciclo == 10:
        break

#Abaixo, o meu código, adaptado depois de ver a resolução do desafio 51

ciclo = 0
primeiro = int(input('Digite o primeiro número: '))
razao = int(input('Digite a razão da progressão aritmetica: '))
final = primeiro + (10 - 1) * razao
for numero in range(primeiro, final + razao, razao):
    print(numero)
    ciclo += 1
    if ciclo == 10:
        break
