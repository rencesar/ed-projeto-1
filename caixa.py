from fila import Fila


class Caixa:
    def __init__(self, items=None):
        self.items = Fila(items)
        self.valor_total = 0

    def adicionar_item(self, item):
        self.items.add(item)

    def validar_item(self, item):
        return self.items.remover()
    
    def caixa_vazio(self):
        return self.items.vazia()

def menu_caixa(carrinho):
    while not carrinho.vazio():
        item = carrinho.remover_item()
        caixa.adicionar_item()

def imprimir_fila(fila):
    pass