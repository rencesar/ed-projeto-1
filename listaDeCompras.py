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
    
    def rem_inicio(self):
        return self.items.remover_inicio()
    
    def rem_meio(self, pos):
        return self.items.remover_meio(pos)
    
    def rem_fim(self):
        return self.items.remover_fim()
    
    def vazia(self):
        return self.items.vazia()
    
    def get_primeiro(self):
        return self.items.get_cabeca()

    def get_ultimo(self):
        return self.items.get_cauda()

    def total_items(self):
        return self.items.get_total()

def menu_add_item(lista):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\t╔════════════════════════════╗')
    # print('\t║                            ║')
    print('\t║ Adicionando itens na lista ║')
    # print('\t║                            ║')
    print('\t╚════════════════════════════╝')

    item = input('\n»insira o nome do item na lista: ')

    if lista.vazia():
        if lista.adicionar_inicio(item):
            print(f'\n\t»»{item} adicionado com sucesso!')
        else:
            print(f'\n\t»»{item} não adicionado.')
        lixo = input('\n\n\n»precione enter para continuar...')
    
    else:
        print('\n»sua lista:\n')
        
        imprimir_lista(lista)
        
        pos = int(input('\n\t»»selecione a posição do item na lista: '))
        pos -= 1
        
        if pos <= 0:
            if lista.adicionar_inicio(item):
                print('\n\t\t»»»item adicionado com sucesso!')
            else:
                print('\n\t\t»»»item não adicionado.')
            lixo = input('\n\n\n»precione enter para continuar...')
        
        elif pos >= lista.total_items():
            if lista.adicionar_fim(item):
                print('\n\t\t»»»item adicionado com sucesso!')
            else:
                print('\n\t\t»»»item não adicionado.')
            lixo = input('\n\n\n»precione enter para continuar...')
        
        else:
            if lista.adicionar_posicao(item, pos):
                print('\n\t\t»»»item adicionado com sucesso!')
            else:
                print('\n\t\t»»»item não adicionado.')
            lixo = input('\n\n\n»precione enter para continuar...')

def menu_remover_item(lista):
    if lista.vazia():
        print('\n\t»»não pode mais remover, lista vazia.')
        lixo = input('\n\n\n»precione enter para continuar...')
    
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\t╔══════════════════════════╗')
        print('\t║ Removendo itens da lista ║')
        print('\t╚══════════════════════════╝')

        print('»sua lista:\n')

        imprimir_lista(lista)

        pos = int(input('\n\t»»selecione o item a ser removido: '))

        if pos <= 1:
            if lista.remover_inicio():
                print('\n\t\t»»»item removido com sucesso!')
            else:
                print('\n\t\t»»»item não removido.')
            lixo = input('\n\n\n»precione enter para continuar...')
    
        elif pos >= lista.total_items():
            if lista.remover_fim():
                print('\n\t\t»»»item removido com sucesso!')
            else:
                print('\n\t\t»»»item não removido.')
            lixo = input('\n\n\n»precione enter para continuar...')
    
        else:
            pos -= 1
            if lista.remover_meio(pos):
                print('\n\t\t»»»item removido com sucesso!')
            else:
                print('\n\t\t»»»item não removido.')
            lixo = input('\n»precione enter para continuar...')

def imprimir_lista(lista):
    if lista.vazia():
        print('\n\t»»lista ainda vazia, adicione itens.')
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\t╔═════════════════════════╗')
        print('\t║ Exibindo itens da lista ║')
        print('\t╚═════════════════════════╝')

        print('\n»sua lista:\n')
        
        aux = lista.get_primeiro()
        count = 1
        while aux is not None:
            print(f'    Posição {count}: {aux}')
            aux = aux.get_proximo()
            count += 1
