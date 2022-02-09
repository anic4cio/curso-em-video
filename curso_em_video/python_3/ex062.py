"""
Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.
"""

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
ciclo = 1
ciclo2 = 10
termos = 0
while ciclo2 != 0:
    termos = termos + ciclo2
    while ciclo < termos:
        print('{} > '.format(termo), end='')
        termo += razao
        ciclo += 1
    print('Pausa')
    ciclo2 = int(input('Quantos termos deseja mostrar a mais? '))
print('Processo finalizado com {} termos exibidos.'.format(termos))


#Consegui fazer sozinho depois de várias tentativas e frustrações, o importante é que eu consegui































# termo = int(input('Digite o termo: '))
# razao = int(input('Digite a razão: '))
# ciclo1 = 1
# quant_termos = 0
# ciclo2 = 10
# while ciclo2 != 0:
#     quant_termos = quant_termos + ciclo2
#     while ciclo1 < quant_termos:
#         print('{}'.format(termo), end=' > ')
#         termo = termo + razao
#         ciclo1 += 1
#     print('PAUSA')
#     ciclo2 = int(input('Quantos termos deseja mostrar a mais? '))
# print('Fim!')
# print('Foram printados {} vezes.'.format(quant_termos))
