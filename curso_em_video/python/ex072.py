numeros_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
                   'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numero = 0
while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if -1 < numero < 21:
        resposta = input(f'Você digitou o número {numeros_extenso[numero]}. \nDeseja fazer outra vez? [S/N] ').strip()[0]
        if resposta in 'Nn':
            print('Progama encerrado.')
            break
    else:
        print('Número inválido.', end=' ')