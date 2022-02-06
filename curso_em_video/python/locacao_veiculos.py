dia = int(input('Quantos dias ficou com o veículo? '))
km = float(input('Quantos quilômetros foram percorridos? '))
tot = (dia * 60) + (km * 0.15)
print('O total do aluguel do veículo foi de R${:.2f}'.format(tot))

