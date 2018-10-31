from library.lista_encadeada import ListaEncadeada

from utils import clean_screen


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
    print('\t╔════════════════════════════╗')
    print('\t║ Adicionando itens na lista ║')
    print('\t╚════════════════════════════╝')

    item = input('\n»insira o nome do item na lista: ')

    if lista.vazia():
        if lista.adicionar_inicio(item):
            print(f'\n\t»»{item} adicionado com sucesso!')
        else:
            print(f'\n\t»»{item} não adicionado.')
        input('\n\n\n»precione enter para continuar...')
        return
    
    clean_screen()
    imprimir_lista(lista)
    
    pos = int(input('\n\t»»selecione a posição do item na lista: '))
    pos -= 1
    
    if pos <= 0:
        if lista.adicionar_inicio(item):
            print('\n\t\t»»»item adicionado com sucesso!')
        else:
            print('\n\t\t»»»item não adicionado.')
        input('\n\n\n»precione enter para continuar...')
    
    elif pos >= lista.total_items():
        if lista.adicionar_fim(item):
            print('\n\t\t»»»item adicionado com sucesso!')
        else:
            print('\n\t\t»»»item não adicionado.')
        input('\n\n\n»precione enter para continuar...')
    
    else:
        if lista.adicionar_posicao(item, pos):
            print('\n\t\t»»»item adicionado com sucesso!')
        else:
            print('\n\t\t»»»item não adicionado.')
        input('\n\n\n»precione enter para continuar...')


def menu_remover_item(lista):
    if lista.vazia():
        print('\n\t»»não pode mais remover, lista vazia.')
        input('\n\n\n»precione enter para continuar...')
        return

    print('\t╔══════════════════════════╗')
    print('\t║ Removendo itens da lista ║')
    print('\t╚══════════════════════════╝')

    print('»sua lista:\n')

    imprimir_lista(lista)

    pos = int(input('\n\t»»selecione o item a ser removido: '))
    pos -= 1

    if pos <= 1:
        if lista.rem_inicio():
            print('\n\t\t»»»item removido com sucesso!')
        else:
            print('\n\t\t»»»item não removido.')
        input('\n\n\n»precione enter para continuar...')

    elif pos >= lista.total_items():
        if lista.rem_fim():
            print('\n\t\t»»»item removido com sucesso!')
        else:
            print('\n\t\t»»»item não removido.')
        input('\n\n\n»precione enter para continuar...')

    else:
        if lista.rem_meio(pos):
            print('\n\t\t»»»item removido com sucesso!')
        else:
            print('\n\t\t»»»item não removido.')
        input('\n»precione enter para continuar...')

def imprimir_lista(lista):
    if lista.vazia():
        print('\n\t»»lista ainda vazia, adicione itens.')
        return

    print('\t╔═════════════════════════╗')
    print('\t║ Exibindo itens da lista ║')
    print('\t╚═════════════════════════╝')

    print('\n»sua lista:\n')
    
    p = lista.get_primeiro()
    count = 1
    print('╔═════════════╗')
    while p is not None:
        print(f'║ »{count}° posição ║ → {p}')
        print('╠═════════════╣')
        p = p.get_proximo()
        count += 1
