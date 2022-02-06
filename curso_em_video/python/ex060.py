#Esse é difícil, mas borá lá
#Tentei sozinho e não consegui,  assisti o vídeo da resposta e tô tentando agora 20/01/22
numero = int(input('Digite o número: '))
fatorial = 1
for numero in range(numero, 0, -1):
    print('{}'.format(numero), end='')
    print(' x ' if numero > 1 else ' = ', end='')
    fatorial *= numero
print(fatorial)

#Preciso tentar fazer de novo amanhã
#Tá hard
