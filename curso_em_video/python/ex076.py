produtos = ('Volante G29', 1890, 'Banco Bride', 1779, 'Kit Monitores 4k', 9789, 'Pedais Hidraulicos',
            919, 'Câmbio', 1599, 'Nobreak', 1100, 'Mesa articulada', 1900, 'Kit roupa', 499)
for items in range(0, 16, 2):
    print(f'{produtos[items]:.<30}', f'R$ {produtos[items+1]:>7.2f}')
