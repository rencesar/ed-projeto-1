from no import No


class Fila:
    # INICANDO A FILA
    def __init__(self, itens=[]):
        self._itens = itens

    # FILA VAZIA
    def vazia(self):
        if self._itens == []:
            return True
        return False

    # INSERINDO NA FILA
    def add(self, item):
        self._itens.insert(0, item)

    # REMOVENDO DA FILA
    def remover(self):
        return self._itens.pop()

    # RETORNANDO O TAMANHO DA FILA
    def tamanho(self):
        return len(self._itens)
