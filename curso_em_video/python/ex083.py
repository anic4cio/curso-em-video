conta = str(input('Digite uma expressão matemática: '))
parenteses = []
for p in conta:
    if p == '(':
        parenteses.append(p)
    elif p == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(p)
if len(parenteses) == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')

