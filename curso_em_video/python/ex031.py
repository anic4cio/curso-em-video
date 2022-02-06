dist = float(input('Quantos quilômetros foram percorridos na sua viagem? '))
if dist <= 200:
    dist = dist * 0.50
    print('O valor total da sua viagem foi de R${:.2f}'.format(dist))
else:
    dist = dist * 0.45
    print('O valor total da sua viagem com valor promocional foi R${:.2f}'.format(dist))

