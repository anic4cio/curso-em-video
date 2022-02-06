lista = []
lista_par = []
lista_impar = []
continuar = 1
while continuar != 0:
    numero = int(input('Digite um número: '))
    lista.append(numero)
    continuar = int(input('Pressione 1 para continuar ou 0 para sair: '))
for numero in lista:
    if numero % 2 == 0:
        lista_par.append(numero)
    elif numero % 2 == 1:
        lista_impar.append(numero)
print(f'Lista com todos o números: {lista}')
print(f'Lista de pares: {lista_par}')
print(f'Lista de ímpares: {lista_impar}')
