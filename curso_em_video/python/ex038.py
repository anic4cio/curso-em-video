numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
if numero1 > numero2:
    print('O número {} é maior que o número {}'.format(numero1, numero2))
elif numero1 < numero2:
    print('O número {} é maior que o número {}'.format(numero2, numero1))
else:
    print('Os números são idênticos!')
