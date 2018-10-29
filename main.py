from no import No
from lista_encadeada import ListaEncadeada
from pilha import Pilha
from fila import Fila
from listaDeCompras import ListaCompras, menu_add_item, menu_remover_item, imprimir_lista
import os

opcao = 0
lista = ListaCompras()
carrinho = Carrinho()

while opcao != 4:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\t########################################')
    print('\t#                                      #')
    print ('\t#    1º: Fazendo a lista de compras    #')
    print('\t#                                      #')
    print('\t########################################\n')

    print('\t\t#########################')
    print('\t\t# 1 - Adionar item      #')
    print('\t\t# 2 - Remover item      #')
    print('\t\t# 3 - Ver a lista       #')
    print('\t\t# 4 - Ir para o caixa   #')
    print('\t\t#########################')

    opcao = int(input('\n>sua opção: '))

    if opcao < 1 or opcao > 4:
        print('\n    >>pção inválida!!')
        opcao = int(input('    >>selecione uma opção novamente: '))

    elif opcao == 1:
        menu_add_item(lista)

    elif opcao == 2:
        menu_remover_item(lista)

    elif opcao == 3:
        imprimir_lista(lista)
        input('\n>precione enter para continuar...')

    elif opcao == 4:
        if lista.vazia():
            print('\n    >>lista vazia, tente adicionar itens para finalizar.')
            item = input('\n\t>>>insira seu item no carrinho: ')
            menu_add_item(lista)
            opcao = 1
        else:
            print('\n    >>lista finalizada, se direcione ao supermercado!')