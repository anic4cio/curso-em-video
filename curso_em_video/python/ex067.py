tabuada = int(input('Quer ver a tabuada de que número: '))
while True:
    for i in range(1, 11):
        print(f'{tabuada} x {i:2} = {i * tabuada}')
    print(10*'~-')
    tabuada = int(input('Quer ver mais alguma tabuada? \nDigite o número para ver a tabuada  \nOu número negativo para sair: '))
    if tabuada < 0:
        print('\nPrograma encerrado.')
        break
