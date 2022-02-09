"""
Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
"""

cid = str(input('Em que cidade você nasceu: ')).title().strip()
print(cid.split()[0] == 'Santo')
