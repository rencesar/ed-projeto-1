from no import No


class Fila:
    # INICANDO A FILA
    def __init__(self, itens=[]):
        self._cabeca = None
        for item in itens:
            self.add(item)

    # FILA VAZIA
    def vazia(self):
        return self.tamanho() != 0

    # INSERINDO NA FILA
    def add(self, item):
        item = No(item)
        if self._cabeca is not None:
            self._cabeca.set_proximo(item)
        self._cabeca = item

    # REMOVENDO DA FILA
    def remover(self):
        aux = self._cabeca
        if aux is None:
            raise ValueError("Fila vazia")
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
