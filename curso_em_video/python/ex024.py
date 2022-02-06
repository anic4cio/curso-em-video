# cid = input('Qual cidade você mora? ').strip()
# cid = cid.lower()
# cid = cid.split()
# if cid[0] == 'santo':
#     print('True')
# else:
#     print('False')

#Melhor forma

cid = input('Digite uma cidade: ').strip()
print(cid.lower() == 'santo')

#No dia seguinte

cid = str(input('Em que cidade você nasceu: ')).title().strip()
print(cid.split()[0] == 'Santo')
