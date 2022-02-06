opcao = str('')
total_numeros = media = soma = 0
while opcao != 'N':
    numero = int(input('Digite um número: '))
    if total_numeros == 0:
        maior = menor = numero
    elif numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    total_numeros += 1
    soma += numero
    opcao = input('Deseja continuar? [S/N] ').upper()
media = soma / total_numeros
print('Você digitou {} números e a média foi {:.2f}'.format(total_numeros, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
