matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for x in range(0, 3):
    for t in range(0, 3):
        matriz[x][t] = (int(input(f'Digite um valor para {[x, t]}: ')))
for x in range(0, 3):
    for t in range(0, 3):
        print(f'[{matriz[x][t]:^6}]', end=' ')
    print()