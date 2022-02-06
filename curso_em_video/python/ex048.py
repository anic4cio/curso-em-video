soma = 0
contador = 0
for numeros in range(1, 500, 2):
    if numeros % 3 == 0:
        soma += numeros
        contador += 1
print(soma)
print(contador)
