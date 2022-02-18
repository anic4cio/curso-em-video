"""
Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos 
e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)
"""

from asyncio import TimerHandle
from datetime import timedelta


def notas(*nota, sit=False):
    """
    -> Função de análise de notas.
    :param notas: Variável para tribuição de notas (quantidade indefinida).
    :param sit: Parâmetro para mostrar ou não a situação proveniente da média das notas.        
    :return: Dicionário com todas as informações informadas.
    """
    info = dict()
    info['total_notas'] = len(nota)
    info['maior'] = max(nota)
    info['menor'] = min(nota)
    info['media'] = sum(nota) / info['total_notas']
    if sit:
        if info['media'] > 8:
            info['sit'] = 'Ótimo'
        elif info['media'] > 6:
            info['sit'] = 'Bom'
        elif info['media'] > 4:
            info['sit'] = 'Regular'
        else:
            info['sit'] = 'Recuperação'
    return info


prova = notas(7.5, 5.7, 6.9, sit=True)
print(prova)