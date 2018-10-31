from no import No
from lista_encadeada import ListaEncadeada
from pilha import Pilha
from fila import Fila
from listaDeCompras import ListaCompras, menu_add_item, menu_remover_item, imprimir_lista
from carrinho import Carrinho, add_carrinho, remover_item_carrinho, imprimir_pilha
from caixa import Caixa
import os

opcao = 0
lista = ListaCompras()
carrinho = Carrinho()
caixa = Caixa()

# menu lista
while opcao != 4:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\t╔════════════════════════════════╗')
    print('\t║ 1º: Fazendo a lista de compras ║')
    print('\t╠════════════════════════════════╣')
    print('\t║ Opção 1 »» adionar item        ║')
    print('\t║ Opção 2 »» remover item        ║')
    print('\t║ Opção 3 »» ver a lista         ║')
    print('\t║ Opção 4 »» ir para o mercado   ║')
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

# menu pilha
while not lista.vazia():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\t╔═════════════════════════════════════╗')
    print('\t║ 2º: Colocando itens no carrinho     ║')
    print('\t╠═════════════════════════════════════╣')
    print('\t║ Opção 1 »» adionar item             ║')
    print('\t║ Opção 2 »» remover item             ║')
    print('\t║ Opção 3 »» exibir itens do carrinho ║')
    print('\t╚═════════════════════════════════════╝')
    
    opcao = int(input('\n»sua opção: '))

    if opcao < 1 or opcao > 3:
        print('\n\t»opção inválida!!')
        opcao = int(input('\t»selecione uma opção novamente: '))

    elif opcao == 1:
        add_carrinho(lista, carrinho)

    elif opcao == 2:
        remover_item_carrinho(carrinho)

    elif opcao == 3:
        imprimir_pilha(carrinho)
        lixo = input('\n\n\n»precione enter para continuar...')

aux = No()
while not carrinho.vazio():
    aux = carrinho.get_primeiro()
    caixa.adicionar_item(aux)
    carrinho.remover_item()

# menu fila
while not caixa.caixa_vazio():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\t╔════════════════════════════════════════════╗')
    print('\t║ 3º: Passando no caixa os itens do carrinho ║')
    print('\t╚════════════════════════════════════════════╝')

    input('VAI TOMAR NO CU ')