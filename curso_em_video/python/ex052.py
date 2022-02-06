while True:
    primo = 0
    numero = int(input('Digite um número inteiro e verifique se é primo: '))
    for contagem in range(1, numero + 1):
        if numero % contagem == 0:
            primo += 1
    if primo == 2:
        print('\033[32mO número {} é um número primo.\033[m'.format(numero))
    if primo > 2 or primo == 1:
        print('\033[31mO número {} não é primo.\033[m'.format(numero))

#Eu não consegui fazer de primeira, porém assisti o vídeo, compreendi a lógica e com um pouco de dificuldade consegui escrever meu algoritmo.