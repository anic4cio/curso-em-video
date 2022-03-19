"""
Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
"""

def site_conect(site):
    from urllib import request
    try:
        request.urlopen(f'http://{site}')
    except:
        print('Este site não está acessível.')
    else:
        print('Site acessado com sucesso.')


site_conect(str(input('Digite o site: ')))