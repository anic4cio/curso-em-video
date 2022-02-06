lado1 = float(input('Digite a primeira linha do triângulo: '))
lado2 = float(input('Digite a segunda linha do triângulo: '))
lado3 = float(input('Digite a terceira linha do triângulo: '))
tipo_triangulo = ''
if lado1 >= (lado2 + lado3) or lado2 >= (lado1 + lado3) or lado3 >= (lado1 + lado2):
    tipo_triangulo = 'Estas linhas não podem formar um triângulo!'
elif lado1 == lado2 and lado2 == lado3:
    tipo_triangulo = 'Triângulo Equilátero: Todos os lados iguais.'
elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
#elif lado1 == lado2 == lado3: também pode fazer assim
    tipo_triangulo = 'Triângulo Esósceles: Dois lados iguais.'
else:
    tipo_triangulo = 'Triângulo Escaleno: Todos os lados diferentes.'
print(tipo_triangulo)
