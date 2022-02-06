valor_emprestimo = float(input('Qual o valor do empréstimo o senhor deseja? R$'))
salario = float(input('Qual o seu salário atual? R$'))
anos = int(input('Em quantos anos será realizado o pagamento? '))
meses = anos * 12
prestacao = valor_emprestimo / meses
if (salario * 0.30) < prestacao:
    print('\033[31mEmpréstimo negado. A prestação de R${:.2f} precisa ser menor que 30% do seu salário!'.format(prestacao))
else:
    print('\033[32mEmpréstimo Aceito. O valor de R${:.2f} estará na sua conta em até 30 minutos!'.format(valor_emprestimo))
