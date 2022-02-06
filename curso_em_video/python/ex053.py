frase = str(input('Digite uma frase: ')).replace(' ', '').upper()
frase_invertida = frase[::-1]
print('A frase "{}" inverdida fica "{}".'.format(frase, frase_invertida))
if frase_invertida == frase:
    print('Sim, sua frase é um palíndromo, ela pode ser lida de trás pra frente.')
else:
    print('Sua frase não é um palíndromo, é uma frase comum!')


#Esquema para manipular espaços de uma frase

# frase = str(input('Digite: ')).upper()
# palavras = frase.split()
# junto = '&'.join(palavras)
# print(frase)
# print(palavras)
# print(junto)