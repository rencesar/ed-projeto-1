from no import No


class ListaEncadeada:
    # INICIANDO A LISTA
    def __init__(self, cabeca=None, cauda=None):
        self._cabeca = cabeca
        self._cauda = cauda
        self.total = 1

    # VERIFICA SE A LISTA ESTA VAZIA
    def vazia(self):
        if self._cabeca == None:
            return True
        return False

    # ADICIONA UM ELEMENTO NO INICIO DA LISTA
    def add_inicio(self, item):
        aux = No(item)
        if self._cabeca == None:
            self._cabeca = self._cauda = aux
            self.count()
            return True
        else:
            aux.set_proximo(self._cabeca)
            self._cabeca = aux
            self.count()
            return True
        return False

    # ADICIONA UM ELEMENTO NO MEIO DA LISTA
    def add_meio(self, item, pos):
        aux = No(item)
        p = q = self._cabeca
        for i in range(pos-1):
            p = p.get_proximo()
            q = p.get_proximo()
        aux.set_proximo(q)
        p.set_proximo(aux)
        self.count()
        return True

    # ADICIONA UM ELEMENTO NO FINAL DA LISTA   
    def add_fim(self, item):
        aux = No(item)
        self._cauda.set_proximo(aux)
        self._cauda = aux
        self.count()
        return True

    # REMOVE O ELEMENTO DO INICIO
    def remover_inicio(self):
        self._cabeca = self._cabeca.get_proximo()
        self.countn()
        return True

    # REMOVE UM ELEMTO DA LISTA
    def remover_meio(self, pos):
        p = q = self._cabeca
        for i in range(pos-1):
            p = p.get_proximo()
            q = p.get_proximo()
        p.set_proximo(q.get_proximo())
        self.countn()
        return True

    # REMOVE O ELEMENTO DO FINAL
    def remover_fim(self):
        p = self._cabeca
        aux = self._cauda
        while p.get_proximo() != self._cauda:
            p = p.get_proximo()
        p.set_proximo(None)
        self.countn()
        return aux and True

    # ACRESCENTA A CADA NOVO ITEM
    def count(self):
        self.total+=1

    # DECRESCENTA A CADA REMOÇÃO
    def countn(self):
        self.total-=1

    # TOTAL DE ITENS NA LISTA
    def get_total(self):
        return self.total-1

    def get_cauda(self):
        return self._cauda

    def imprimir(self):
        aux = self._cabeca
        count = 1
        while aux:
            print('    {}° - {}'.format(count, aux.get_dado()))
            aux = aux.get_proximo()
            count += 1
