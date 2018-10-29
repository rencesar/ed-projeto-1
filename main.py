from fila import Fila
from lista_encadeada import ListaEncadeada
from carrinho import Carrinho
from listaDeCompras import add_item, remover_item, imprimir_lista
import os

opcao = 0
lista = ListaEncadeada()
carrinho = Carrinho()

while opcao != 4:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\t########################################')
    print('\t#                                      #')
    print('\t#    1º: Fazendo a lista de compras    #')
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
        print('\n    >>opção inválida!!')
        opcao = int(input('    >>selecione uma opção novamente: '))
    if opcao == 1:
        item = input('\n    >>insira seu item na lista: ')
        add_item(lista, item)
    elif opcao == 2:
        if lista.vazia():
            print('\n    >>não pode mais remover, lista vazia.')
            input('\n>precione enter para continuar...')
        else:
            remover_item(lista)
    elif opcao == 3:
        if lista.vazia():
            print('\n    >>lista ainda vazia, adicione itens.')
            input('\n>precione enter para continuar...')
        else:
            imprimir_lista(lista)
    elif opcao == 4:
        if lista.vazia():
            print('\n    >>lista vazia, tente adicionar itens para finalizar.')
            item = input('\n\t>>>insira seu item no carrinho: ')
            add_item(lista, item)
            opcao = 1
        else:
            print('\n    >>lista finalizada, se direcione ao caixa!')
        # inverter o vetor
        # colocar os itens na pilha;