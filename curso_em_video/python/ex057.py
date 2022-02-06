# sexo = ''
# while sexo != 'M' and sexo != 'F':
#     sexo = str(input('\033[1mDigite seu sexo: [M/F] \033[m')).strip().upper()[0]
#     if sexo != 'M' and sexo != 'F':
#         print('\033[31mDado inválido. Digite novamente.\033[m')
# print('\033[32mSexo registrado com sucesso!\033[m')

#Outra resolução interessante do Guanaraba

sexo = str(input('\033[1mDigite seu sexo: [M/F] \033[m')).strip().upper()[0]
# 1 Enquanto sexo não for M, m, F ou f.
while sexo not in 'MmFf':
    # 2 Repita o loop
    sexo = str(input('Inválido. Informe seu sexo: '))
print('Sexo {} registrado com sucesso'.format(sexo))
