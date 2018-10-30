from no import No


class Pilha:

    # INICIANDO A PILHA
    def __init__(self, topo=None):
        self._topo = topo
    
    # PILHA VAZIA
    def vazia(self):
        return self._topo is None
    
    # INSERINDO NA PILHA
    def add(self, item):
        aux = No(item)
        if self._topo is None:
            self._topo = aux
            return True
        aux.set_proximo(self._topo)
        self._topo = aux
        return True
    
    # REMOVENDO O ELEMENTO DO TOP
    def remover(self):
        if self._topo is None:
            raise IndexError("Nao contem elemento.")
        self._topo = self._topo.get_proximo()
        return True
    
    # RETORNANDO O TAMANHO DA PILHA
    def tamanho(self):
        count = 0
        if self._topo is None:
            return count
        aux = self._topo
        while aux.get_proximo() is not None:
            aux = aux.get_proximo()
            count += 1
        return count
    
    # RETORNANDO O ELEMENTO DO TOP
    def get_topo(self):
        return self._topo
