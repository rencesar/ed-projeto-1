import os
from library.pilha import Pilha
from list_de_compras import imprimir_lista

from utils import clean_screen

class Carrinho:
    def __init__(self, items=None):
        self.items = Pilha(items)
    
    def colocar_item(self, item):
        self.items.add(item)
    
    def remover_item(self):
        return self.items.remover()
    
    def vazio(self):
        return self.items.vazia()

    def get_tamanho(self):
        return self.items.tamanho()
    
    def get_primeiro(self):
        return self.items.get_topo()

def add_carrinho(lista, pilha):
    imprimir_lista(lista)
    
    print('\n\t╔═══════════════════════════════╗')
    print('\t║ Adicionando itens no carrinho ║')
    print('\t╚═══════════════════════════════╝')
    
    pos = int(input('\n»informe a posição do item na lista para colocar no carrinho: '))

    if pos > lista.total_items() or pos < 1:
        print('»posição invalida!')
        pos = int(input('»escolha uma nova posição: '))

    elif pos <= 1:
        pilha.colocar_item(lista.get_primeiro())
        lista.rem_inicio()
    
    elif pos >= lista.total_items():
        pilha.colocar_item(lista.get_ultimo())
        lista.rem_fim()
    
    else:
        pos -= 1
        aux = lista.get_primeiro()
        for i in range (pos):
            aux = aux.get_proximo()
        pilha.colocar_item(aux)
        lista.rem_meio(pos)

def remover_item_carrinho(pilha):

    if pilha.vazio():
        print('\n\t»»lista ainda vazia, adicione itens.')
        return
    
    imprimir_carrinho(pilha)
    
    print('\n\t╔═════════════════════════════════╗')
    print('\t║ »deseja remover o item do topo? ║')
    print('\t╠═════════════════════════════════╣')
    print('\t║ Opção 1 »» remover item         ║')
    print('\t║ Opção 2 »» voltar               ║')
    print('\t╚═════════════════════════════════╝')

    opcao = int(input('\n»sua opção: '))

    if opcao == 1:
        pilha.remover_item()
        print('\n\t»»item removido!')
        input('\n\n\n»precione enter para continuar...')

    elif opcao == 2:
        print('\n\t»»item não removido!')
        input('\n\n\n»precione enter para continuar...')
    
    else:
        print('\n\t»»opção inválida!')
        opcao = int(input('\n»tente uma nova opção: '))

def imprimir_carrinho(carrinho):
    if carrinho.vazio():
        print('\n\t»»carrinho ainda vazio, adicione itens.')
        return

    print('\t╔════════════════════════════╗')
    print('\t║ Exibindo itens do carrinho ║')
    print('\t╚════════════════════════════╝')

    print('\n»seu carrinho:\n')

    aux = carrinho.get_primeiro()
    print('╔═════════╗')
    print('║ »topo ↓ ║')
    print('╠═════════╝')
    while aux is not None:
        print(f'║   → {aux}')
        aux = aux.get_proximo()
    print('╠═════════╗')
    print('║ »fim  ↑ ║')
    print('╚═════════╝')