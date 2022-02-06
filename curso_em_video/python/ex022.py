nome = str(input('Digite seu nome e sobrenome: ')).strip()
prim = nome.split()
print('Seu nome em maiúscula é {}'.format(nome.upper()))
print('Em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e possui {} letras'.format(prim[0], len(prim[0])))

#Fiz o mesmo código no dia seguinte

nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em letras maiúsculas é {}.'.format(nome.upper()))
print('Em letras minúsculas fica {}.'.format(nome.lower()))
print('Seu nome completo tem {} letras.'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome é {} e tem {} letras'.format(nome.split()[0], len(nome.split()[0])))
