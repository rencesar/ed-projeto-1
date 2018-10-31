from no import No


class Fila:
    # INICANDO A FILA
    def __init__(self, cabeca=None):
        self._cabeca = cabeca
    
    # PEGAR PRIMEIRO ELEMENTO
    def get_primeiro(self):
        return self._cabeca

    # FILA VAZIA
    def vazia(self):
        return self._cabeca is None

    # INSERINDO NA FILA
    def add(self, item):
        aux = No(item)
        if self._cabeca is None:
            self._cabeca = aux
        else:
            aux = self._cabeca
            while True:
                if aux.get_proximo() is None:
                    break
                aux = aux.get_proximo()
            aux.set_proximo(item)

    # REMOVENDO DA FILA
    def remover(self):
        if aux is None:
            raise ValueError("Fila vazia")
        aux = self._cabeca
        self._cabeca = self._cabeca.get_proximo()
        return aux

    # RETORNANDO O TAMANHO DA FILA
    def tamanho(self):
        aux = self._cabeca
        count = 0
        while aux is not None:
            aux = aux.get_proximo()
            count += 1
        return count
