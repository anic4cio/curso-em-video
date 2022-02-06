# salario = float(input('Digite seu salário atual: '))
# if salario <= 1250:
#     reajuste_salarial = salario * 0.15
#     print('Seu salário atual agora é R${}'.format(salario + reajuste_salarial))
# else:
#     reajuste_salarial = salario * 0.10
#     print('Seu salário atual agora é de {} reais'.format(salario + reajuste_salarial))

#Vi essa outra forma nos comentários

salario = float(input('Digite seu salário atual: '))
if salario <= 1250:
    salario = salario * 1.15
    print('Seu salário atual agora é R${:.2f}'.format(salario))
else:
    salario = salario * 1.10
    print('Seu salário atual agora é de {:.2f} reais'.format(salario))
