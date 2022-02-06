print('~~~ANALISTA DE TRIÂNGULOS~~~')
reta1 = float(input('Digite a primeira reta: '))
reta2 = float(input('A segunda reta: '))
reta3 = float(input('Agora a terceira reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Esses valores podem formar um triângulo!')
else:
    print('Esses valores não formam um triângulo.')
