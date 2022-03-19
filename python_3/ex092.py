"""
Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de
trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente
de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""

dados = {}
dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
idade = 2022 - nascimento
dados['idade'] = idade
ctps = int(input('Cartera de Trabalho: (digite 0 se não tiver) '))
dados['ctps'] = ctps
if ctps != 0:
    dados['contratacao'] = int(input('Ano de Contratação: '))
    dados['salario'] = int(input('Salário: R$ '))
    dados['aposentadoria'] = (dados['contratacao'] - nascimento) + 35
print('~-' * 20)
print(f'Nome é {dados["nome"]}')
print(f'Idade é {idade}')
print(f'Carteira de Trabalho é {dados["ctps"]}')
if ctps != 0:
    print(f'O ano de contratação foi {dados["contratacao"]}')
    print(f'O salário é R${dados["salario"]}')
    print(f'O ano de aponsentadoria será {dados["aposentadoria"]}')
print(dados)
