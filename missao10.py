# def receber_nome():
#     nome = input('Digite um nome: ')
#     contar_letras = len(nome)
#     return nome, contar_letras


# nome, contar_letras = receber_nome()
# print(f'O nome {nome} tem {contar_letras} letras.')


def contar_letras():
    nome = input('Digite um nome: ')
    print(f'O nome {nome} tem {len(nome)} letras.')


contar_letras()
