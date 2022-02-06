# '*' mostra a lista sem os colchetes, e sep é a string entre as variáveis da lista
print(*num, sep= ', ')
input:[1, 2, 3]
output: 1, 2, 3

# Resumão Não executável Comentado


lanche = list[]
lanche.append('valor') #inclui valor na última posição
lanche.insert(0,'valor') #substitui valor na posição '0'
del lanche[3]
lanche.pop() #elimina o último e reposiciona os valores na lista
if 'valor' in lanche: #evita msg de erro
  lanche.remove('valor') #evita msg de erro
lista2 = list(range(4,11)) #lista2 = [4,5,6,7,8,9,10]
lista3 = [8,5,4,3,0]
lista3.sort() #ordenar valores [0,3,4,5,8]
lista3.sort(reverse=True) #ordenar valores de forma inversa [8,5,4,3,0]
len(lista3) # resposta: 5


Resumão Comentado
num = [2,5,9,1,7]
#num1 = num #link entre lista num e num1
#num1[1]=6
num1=num[:] #gera uma cópia de num
num1[1]=6,8
print(num1)
#num.append(8) #adiciona '8'
#num[0]=3 #substitui a posição 0 pelo valor '3'
#num.sort(reverse=True) #ordena de forma inversa
#num.insert(2,4) #adiciona valor '4' após a posição 2 reordenando a lista
#num.pop() #exclui o último valor '8'
#num.pop(4) #exclui o valor na posição 2 por '1'
print(f'Lista primária: {num}')
print('Excluído valor: {}, Nova lista: {}'.format(num.pop(4),num))
if (9) in num: #Atenção
  num.remove(9) #Muita Atenção
  num.append(0) #Importante
print(f'Condição verificada: {num}' if (1) and (2) or (6) in num else 'Condição não se aplica!') #Importante

print(f'Lista verificada: {num}')
num.sort()
print(f'Lista ordenada: {num}')
print(f'Lista com {len(num)} elementos.')


 Resumão (Bônus)


num1 = list()
num1.append(1),num1.append(4),num1.append(5),num1.append(3)


for c, v in enumerate(num1):
  print(f'Na {c+1}ª posição temos o valor: {v}.')
print('Informe mais 6 (seis) valores!')
for c in range(0,6):
  num1.append(int(input(f'Informe {c+5}º valor: ')))
print(f'{num1}')
for c, v in enumerate(num1):
  print(f'Na posição {c+1} temos o valor: {v}.')