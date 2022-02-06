numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro: '))
if numero1 > numero3 and numero1 > numero2:
    print('{}'.format(numero1))
elif numero2 > numero3 and numero2 > numero1:
    print('{}'.format(numero2))
elif numero3 > numero2 and numero3 > numero1:
    print('{}'.format(numero3))

#não funciona assim:
# if numero1 > numero2 and numero3:

