velo = float(input('Qual velocidade você passou pelo radar: '))
if velo > 80:
    print('Você foi multado em R${:.2f} por dirigir acima da velocidade!'.format((velo - 80)*7))
else:
    print('Diriga com conciência, boa viagem!')

