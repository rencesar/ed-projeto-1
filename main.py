from no import No
from lista_encadeada import ListaEncadeada
from pilha import Pilha
from fila import Fila
from listaDeCompras import ListaCompras, menu_add_item, menu_remover_item, imprimir_lista
from carrinho import Carrinho, add_carrinho, imprimir_pilha
import os

opcao = 0
lista = ListaCompras()
carrinho = Carrinho()

while opcao != 4:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\t╔════════════════════════════════╗')
    print('\t║ 1º: Fazendo a lista de compras ║')
    print('\t╠════════════════════════════════╣')
    print('\t║ Opção 1: Adionar item          ║')
    print('\t║ Opção 2: Remover item          ║')
    print('\t║ Opção 3: Ver a lista           ║')
    print('\t║ Opção 4: Ir para o mercado     ║')
    print('\t╚════════════════════════════════╝')

    opcao = int(input('\n»sua opção: '))

    if opcao < 1 or opcao > 4:
        print('\n\t»opção inválida!!')
        opcao = int(input('\t»selecione uma opção novamente: '))

    elif opcao == 1:
        menu_add_item(lista)

    elif opcao == 2:
        menu_remover_item(lista)

    elif opcao == 3:
        imprimir_lista(lista)
        lixo = input('\n\n\n»precione enter para continuar...')

    elif opcao == 4:
        if lista.vazia():
            print('\n\t»»lista vazia, tente adicionar itens para finalizar.')
            item = input('\n\t»»insira seu item no carrinho: ')
            menu_add_item(lista)
            opcao = 1
        else:
            print('\n\t»»lista finalizada, se direcione ao supermercado!')

while lista.vazia() is not True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\t╔═══════════════════════════════════╗')
    print('\t║ 2º: Colocando itens no carrinho   ║')
    print('\t╠═══════════════════════════════════╣')
    print('\t║ Opção 1: Adionar item             ║')
    print('\t║ Opção 2: Deixar item no carrinho  ║')
    print('\t║ Opção 3: Exibir itens no carrinho ║')
    print('\t╚═══════════════════════════════════╝')
    
    opcao = int(input('\n»sua opção: '))

    if opcao < 1 or opcao > 4:
        print('\n\t»opção inválida!!')
        opcao = int(input('\t»selecione uma opção novamente: '))

    elif opcao == 1:
        add_carrinho(lista, carrinho)

    elif opcao == 2:
        pass

    elif opcao == 3:
        imprimir_pilha(carrinho)
        lixo = input('\n\n\n»precione enter para continuar...')

print('\t\nFILA DE COMPRAS AQUI !!')