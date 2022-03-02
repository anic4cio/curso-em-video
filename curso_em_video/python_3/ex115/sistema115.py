"""
Exercício Python 115a: Vamos criar um menu em Python, usando modularização.
Exercício Python 115b: Vamos ver como fazer acesso a arquivos usando o Python.
Exercício Python 115c: Vamos finalizar o projeto de acesso a arquivos em Python.
"""

from modulo.interface import *
from modulo.arquivo import *
from time import sleep


arq = 'banco_de_dados.txt'
if not arquivoexiste(arq):
    criararquivo(arq)


cabecalho('CADASTRO DE USUÁRIOS')
print('Cadastrar novo usuário...............[1]')
print('Visualizar cadastros.................[2]')
print('Sair.................................[3]')
while True:
    option = str(input('Escolha sua opção: ')).strip()
    if option not in '123' or option == '':
        sleep(0.6)
        option = str(input('Digite uma opção válida: '))
    elif option == '1':
        sleep(0.6)
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif option == '2':
        sleep(0.6)
        cabecalho('CADASTROS REALIZADOS')
        lerarquivo(arq)
    elif option == '3':
        sleep(0.6)
        cabecalho('SISTEMA ENCERRADO')
        break
