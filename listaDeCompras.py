import os
from library import No, Pilha, Fila, ListaEnc

def add_item(lista, item):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\t#########################################')
    print('\t#                                       #')
    print('\t#   Adicionando produtos no carrinho    #')
    print('\t#                                       #')
    print('\t#########################################\n')

    if lista.vazia():
        if lista.add_inicio(item):
            print(f'\t>{item} adicionado com sucesso!')
        else:
            print(f'\t>{item} não adicionado.')
        input('\n>precione enter para continuar...')
    elif lista.get_total() == 1:
        if lista.add_fim(item):
            print(f'\t>{item} adicionado com sucesso!')
        else:
            print('\t>item não adicionado.')
        input('\n>precione enter para continuar...')
    else:
        print('>sua lista:\n')
        lista.imprimir()
        pos = int(input('\n   >>selecione a posição do item na lista: '))
        pos -= 1
        if pos == 0:
            if lista.add_inicio(item):
                print('\n\t>>>item adicionado com sucesso!')
            else:
                print('\n\t>>>item não adicionado.')
            input('\n>precione enter para continuar...')
        elif pos > lista.get_total():
            if lista.add_fim(item):
                print('\n\t>>>item adicionado com sucesso!')
            else:
                print('\n\t>>>item não adicionado.')
            input('\n>precione enter para continuar...')
        else:
            if lista.add_meio(item, pos):
                print('\n\t>>>item adicionado com sucesso!')
            else:
                print('\n\t>>>item não adicionado.')
            input('\n>precione enter para continuar...')

def remover_item(lista):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\t########################################')
    print('\t#                                      #')
    print ('\t#     Removendo itens do carrinho      #')
    print('\t#                                      #')
    print('\t########################################\n')

    print('>sua lista:\n')
    lista.imprimir()

    lixo = int(input('\n    >>selecione o item a ser removido: '))

    if lixo < 1 or lixo > lista.get_total():
        print('\n\t>>>posição não disponível para remoção.')
        input('\n>precione enter para continuar...')
    elif lixo == 1:
        if lista.remover_inicio():
            print('\n\t>>>item removido com sucesso!')
        else:
            print('\n\t>>>item não removido.')
        input('\n>precione enter para continuar...')
    elif lixo == lista.get_total():
        if lista.remover_fim():
            print('\n\t>>>item removido com sucesso!')
        else:
            print('\n\t>>>item não removido.')
        input('\n>precione enter para continuar...')
    else:
        lixo -= 1
        if lista.remover_meio(lixo):
            print('\n\t>>>item removido com sucesso!')
        else:
            print('\n\t>>>item não removido.')
        input('\n>precione enter para continuar...')

def imprimir_lista(lista):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\t########################################')
    print('\t#                                      #')
    print ('\t#   Exibindo a sua lista de compras    #')
    print('\t#                                      #')
    print('\t########################################\n')

    print('>sua lista:\n')
    lista.imprimir()
    input('\n>precione enter para continuar...')