palavras = ('Motard', 'Trilha', 'Liberdade', 'Realização', 'Perseverança', 'Satisfação', 'Conhecimento',
            'Programação', 'Tecnologia', 'Lifestyle')
for p in palavras:
    print(f'\nA palavra {p} tem as vogais: ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')



# palavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis','Estudar', 'Praticar',
#             'Trabalhar', 'Mercado', 'Programador', 'Futuro')
# vogais = 'aeiou'
# for pos in range(0, len(palavras)):
#     qtd_vogais = tuple([c for c in palavras[pos].lower() if c in vogais])
#     print(f'Na palavra {palavras[pos]} temos {" ".join(qtd_vogais)} ')
