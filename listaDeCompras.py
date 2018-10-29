import os
from fila import Fila
from lista_encadeada import ListaEncadeada
from pilha import Pilha


class ListaCompras:

    def __init__(self, items=None):
        self.items = ListaEncadeada(items)
    
    def ordenar_valor(self):
        raise NotImplementedError
    
    def listar_itens(self):
        raise NotImplementedError
    
    def adicionar_inicio(self, item):
        return self.items.add_inicio(item)
    
    def adicionar_posicao(self, item, pos):
        return self.items.add_meio(item, pos)
    
    def adicionar_fim(self, item):
        return self.items.add_fim(item)
    
    def remover_inicio(self):
        return self.items.remover_inicio()
    
    def remover_meio(self, pos):
        return self.items.remover_meio(pos)
    
    def remover_fim(self):
        return self.items.remover_fim()
    
    def vazia(self):
        return self.items.vazia()
    
    def get_primeiro(self):
        return self.items.get_cabeca()

    def total_items(self):
        return self.items.get_total()

def menu_add_item(lista):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\t#########################################')
    print('\t#                                       #')
    print('\t#    Adicionando produtos na lista      #')
    print('\t#                                       #')
    print('\t#########################################\n')

    item = input('\n>insira seu item na lista: ')

    if lista.vazia():
        if lista.adicionar_inicio(item):
            print(f'\n\t>>{item} adicionado com sucesso!')
        else:
            print(f'\n\t>>{item} não adicionado.')
        input('\n>precione enter para continuar...')

    elif lista.total_items() == 1:
        if lista.adicionar_fim(item):
            print(f'\n\t>{item} adicionado com sucesso!')
        else:
            print('\n\t>item não adicionado.')
        input('\n>precione enter para continuar...')
    else:
        print('>sua lista:\n')
        imprimir_lista(lista)
        pos = int(input('\n   >>selecione a posição do item na lista: '))
        pos -= 1
        if pos == 0:
            if lista.adicionar_inicio(item):
                print('\n\t>>>item adicionado com sucesso!')
            else:
                print('\n\t>>>item não adicionado.')
            input('\n>precione enter para continuar...')
        elif pos > lista.total_items():
            if lista.adicionar_fim(item):
                print('\n\t>>>item adicionado com sucesso!')
            else:
                print('\n\t>>>item não adicionado.')
            input('\n>precione enter para continuar...')
        else:
            if lista.adicionar_posicao(item, pos):
                print('\n\t>>>item adicionado com sucesso!')
            else:
                print('\n\t>>>item não adicionado.')
            input('\n>precione enter para continuar...')

def menu_remover_item(lista):
    if lista.vazia():
        print('\n    >>não pode mais remover, lista vazia.')
        input('\n>precione enter para continuar...')
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\t########################################')
        print('\t#                                      #')
        print ('\t#     Removendo itens do carrinho      #')
        print('\t#                                      #')
        print('\t########################################\n')

        print('>sua lista:\n')
        imprimir_lista(lista)

        pos = int(input('\n    >>selecione o item a ser removido: '))

        if pos < 1 or pos > lista.total_items():
            print('\n\t>>>posição não disponível para remoção.')
            input('\n>precione enter para continuar...')
        elif pos == 1:
            if lista.remover_inicio():
                print('\n\t>>>item removido com sucesso!')
            else:
                print('\n\t>>>item não removido.')
            input('\n>precione enter para continuar...')
        elif pos == lista.total_items():
            if lista.remover_fim():
                print('\n\t>>>item removido com sucesso!')
            else:
                print('\n\t>>>item não removido.')
            input('\n>precione enter para continuar...')
        else:
            pos -= 1
            if lista.remover_meio(pos):
                print('\n\t>>>item removido com sucesso!')
            else:
                print('\n\t>>>item não removido.')
            input('\n>precione enter para continuar...')

def imprimir_lista(lista):
    if lista.vazia():
        print('\n    >>lista ainda vazia, adicione itens.')
        input('\n>precione enter para continuar...')
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\t########################################')
        print('\t#                                      #')
        print('\t#   Exibindo a sua lista de compras    #')
        print('\t#                                      #')
        print('\t########################################\n')

        print('>sua lista:\n')
        
        aux = lista.get_primeiro()
        count = 1
        while aux:
            print(f'    {count}° - {aux.get_dado()}')
            aux = aux.get_proximo()
            count += 1
