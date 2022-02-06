from random import randint
print(7 * '~=', 'JOGO DE PAR OU ÍMPAR', 7 * '~=')
vitorias = 0
while True:
    numero = int(input('Digite o seu número: '))
    computador = randint(0, 99)
    par_impar = str(input('Par ou ímpar? [P/I] ')).upper()[0]
    print(25*'~=')
    print(f'Você jogou {numero}\nComputador jogou {computador}')
    print(f'A soma foi de {numero + computador}')
    if (computador + numero) % 2 == 0:
        print(7*'~=', 'RESULTADO DEU PAR', 7*'~=')
    if (numero + computador) % 2 == 1:
        print(7*'~=', 'RESULTADO DEU ÍMPAR', 7*'~=')
    if (numero + computador) % 2 == 0 and par_impar == 'P':
        vitorias += 1
        print('Você ganhou!\n')
    if (numero + computador) % 2 == 1 and par_impar == 'I':
        vitorias += 1
        print('Você ganhou!\n')
    if (numero + computador) % 2 == 1 and par_impar == 'P' or (numero + computador) % 2 == 0 and par_impar == 'I':
        print(f'GAME OVER! Você venceu {vitorias} vezes.')
        break
