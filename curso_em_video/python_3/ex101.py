"""
Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro 
o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, 
OPCIONAL e OBRIGATÓRIO nas eleições.
"""

def voto(nascimento):
    """
    Função que retorna a obrigatoriedade do voto com base no nascimento
    Parâmetro único: Data de nascimento
    """
    nascimento = 2022 - nascimento
    if nascimento > 17 and nascimento < 65:
        return 'voto obrigatório.'
    elif nascimento == 16 or nascimento == 17 or nascimento > 65:
        return 'voto opcional.'
    elif nascimento < 16 :
        return 'não vota.'

