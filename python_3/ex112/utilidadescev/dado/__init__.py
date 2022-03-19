def leiadinheiro(mensagem):
    valido = False
    while not valido:
        entrada = str(input(mensagem)).strip().replace(',', '.')
        if entrada.isalpha() or entrada == '':
            print('\033[0;31mErro! Digite um valor válido.\033[m')
        else:
            valido = True
            return float(entrada)

