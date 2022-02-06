# l1 = float(input('Digite o primeiro lado: '))
# l2 = float(input('Digite o segundo lado: '))
# hipo = (l1 ** 2 + l2 ** 2) ** 0.5
# print('{:.2f}'.format(hipo))

# import math
# l1 = float(input('Digite um lado: '))
# l2 = float(input('Digite outro lado: '))
# hipo = math.hypot(l1, l2)
# print('A hipotenusa é {:.2f}'.format(hipo))

from math import hypot
l1 = float(input('Digite um número: '))
l2 = float(input('Digite outro: '))
hipo = hypot(l1, l2)
print('{:.2f}'.format(hipo))
