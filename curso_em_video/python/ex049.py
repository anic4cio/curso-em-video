tabuada = int(input('Digite o número da tabuada desejado: '))
for multi in range(1, 11):
    print('{} X {:2} = {}'.format(tabuada, multi, (multi * tabuada)))
