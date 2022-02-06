numeros = [[], []]
for c in range(0, 7):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)
print(f'Pares: {sorted(numeros[0])}\nÍmpares: {sorted(numeros[1])}')


