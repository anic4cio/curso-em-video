from random import randint
print('\033[1;94m~Seja bem vindo pequeno gafanhoto, sou seu computador.')
print('~Acabei de pensar num número de 0 a 10. Será que você consegue adivinhar qual é?')
numero_pc = randint(0, 100)
palpite = int(input('~Qual é o seu palpite?\033[m '))
palpites = 1
while palpite != numero_pc:
    if palpite < numero_pc:
        palpite = int(input('\033[1;97mMAIS! Tente novamente: \033[m'))
    if palpite > numero_pc:
        palpite = int(input('\033[1;97mMENOS! Tente novamente: \033[m'))
    palpites += 1
if palpite == numero_pc:
    print('\033[1;92mACERTÔ MIZERAVI! Foram {} tentativas.\033[m'.format(palpites))
