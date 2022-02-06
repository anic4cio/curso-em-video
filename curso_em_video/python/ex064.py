numero = 0
total = 0
ciclo = -1
while numero != 999:
    numero = int(input('Digite um número [999 para parar]: '))
    total += numero
    ciclo += 1
total = total - 999
print('Você digitou {} números e a soma entre eles foi {}'.format(ciclo, total))
