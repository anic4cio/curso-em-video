import random
num = int(input('Tente adivinhar o número que vou pensar de 0 a 5: '))
escolha = random.choice([0, 1, 2, 3, 4, 5])
if num == escolha:
    print('PARABÉNS! VOCÊ ADIVINHOU! NÚMERO {}'.format(escolha))
elif num > 5:
    print('O número é de 0 a 5 meu brother.')
else:
    print('HAHA TROXA, ERROU! Escolhi o número {}'.format(escolha))


#Existe também essa forma de randomizar

from random import randint
print(randint(0,5))
