frase = str(input('Introduza uma frase: ')).lower().strip()
qts = frase.count('a')
qts += frase.count('ã')
pri = frase.find('a')+1
print('A letra A aparece {} vezes na frase'.format(qts))
print('A primeira letra A está na posição {}'.format(pri))
print('A última letra A aparece na posição {}'.format(frase.rfind('a')+1))


#Bora bora que ainda tem acento pra tratar

#Fiz o que o exercício pediu no dia seguinte, porém sem tratar os acentos

frase = str(input('Digite uma frase: ')).strip().lower()
print('A letra "A" aparece {} vezes na frase'.format(frase.count('a')))
print('A primeira letra "A" está na posição {}'.format(frase.find('a')+1))
print('A última letra "A" apareceu na posição {}'.format(frase.rfind('a')+1))
