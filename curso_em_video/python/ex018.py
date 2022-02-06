# import math
# ang = float(input('Digite o ângulo: '))
# sen = math.sin(math.radians(ang))
# cos = math.cos(math.radians(ang))
# tan = math.tan(math.radians(ang))
# print('O ângulo {} tem seno {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(ang, sen, cos, tan))

from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('Ângulo: {:.2g} \nSeno: {:.2g} \nCosseno: {:.2g} \nTangente: {:.2g} \n'.format(ang, sen, cos, tan))
