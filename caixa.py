from fila import Fila

from utils import clean_screen


class Caixa:
    def __init__(self, items=None):
        self.items = Fila(items)
        self.valor_total = 0
    
    def get_primeiro(self):
        self.items.get_primeiro()

    def adicionar_item(self, item):
        self.items.add(item)

    def validar_item(self, item):
        return self.items.remover()
    
    def vazio(self):
        return self.items.vazia()

def menu_caixa(carrinho):
    while not carrinho.vazio():
        item = carrinho.remover_item()
        caixa.adicionar_item()


def imprimir_caixa(caixa):
    if caixa.vazio():
        print('\n\t»»caixa ainda vazio, adicione itens.')
        return

    clean_screen()
    print('\t╔═════════════════════════╗')
    print('\t║ Exibindo itens do caixa ║')
    print('\t╚═════════════════════════╝')

    print('\n»seu caixa:\n')

    aux = caixa.get_primeiro()
    print('╔═════════╗')
    print('║ »topo ↓ ║')
    print('╠═════════╝')
    while aux is not None:
        print(f'║   → {aux}')
        aux = aux.get_proximo()
    print('╠═════════╗')
    print('║ »fim  ↑ ║')
    print('╚═════════╝')