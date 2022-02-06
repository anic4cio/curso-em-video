fibo1 = 0
fibo2 = 1
ciclo = 0
termos = int(input('Digite quantos termos deseja mostrar: '))
while ciclo < termos:
    print(fibo1, end=' > ')
    fibo3 = fibo1 + fibo2
    fibo1 = fibo2
    fibo2 = fibo3
    ciclo += 1
print('Fim')
