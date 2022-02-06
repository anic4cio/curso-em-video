termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
ciclo = 1
while ciclo <= 10:
    print('{} > '.format(termo), end='')
    print(termo, end='')
    print(' > ' if ciclo < 10 else ' > Fim', end='')
    termo += razao
    ciclo += 1
print('Fim')