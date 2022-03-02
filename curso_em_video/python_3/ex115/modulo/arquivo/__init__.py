def arquivoexiste(nome):
    try:
        a = open(nome, 'rt+')
        a.close()
    except:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Erro.')
    else:
        print(f'Arquivo "{nome}" criado.')


def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<31}{dado[1]:>4} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Erro na abertura')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro.')
        else:
            print(f'Registro de {nome} adicionado')
            a.close()



