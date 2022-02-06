vezes = total = 0
while True:
    valor = int(input('Digite um valor: '))
    if valor == 999:
        break
    total += valor
    vezes += 1
print(f'A soma dos {vezes} valores foi {total}')
