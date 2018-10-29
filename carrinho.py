from pilha import Pilha


class Carrinho:
    def __init__(self, items=None):
        self.items = Pilha(items)
    
    def colocar_item(self, item):
        self.items.add(item)
    
    def remover_item(self):
        return self.items.remover()
    
    def vazio(self):
        return self.items.vazia()

    # def add_carrinho(self, lista):
    #     while lista.vazia():
    #         aux = lista.get_cauda()
    #         self.items.add(aux)
    #         lista.remover_fim()

    # def remover_carrinho(self):
    #     while self.items.vazia():
    #         aux = self.items.get_topo()
