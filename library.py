##############
# CLASSE No:
##############
class No:
    # INICIANDO O NO
    def __init__(self, dado=None, proximo=None):
        self._dado = dado
        self._proximo = proximo
    
    # ACESSADORES
    def get_dado(self):
        return self._dado
    def get_proximo(self):
        return self._proximo
    
    # ALTERADORES
    def set_dado(self, valor):
        self._dado = valor
    def set_proximo(self, valor):
        self._proximo = valor

    # PRINT
    def __str__(self):
        return "{}".format(self._dado)
        
##############
# CLASSE LISTA ENCADEADA:
##############
class ListaEnc:
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
        for i in range(pos):
            q = q.get_proximo()
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
        for i in range(pos):
            q = q.get_proximo()
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

    def imprimir(self):
        aux = self._cabeca
        count = 1
        while aux:
            print('    {}° - {}'.format(count, aux.get_dado()))
            aux = aux.get_proximo()
            count += 1

##############
# CLASSE PILHA:
##############
class Pilha:
    # INICIANDO A PILHA
    def __init__(self, topo=None):
        self._topo = topo
    # PILHA VAZIA
    def vazia(self):
        if self._topo == None:
            return True
        return False
    # INSERINDO NA PILHA
    def add(self, item):
        aux = No(item)
        if self._topo == None:
            self._topo = aux
            return True
        else:
            aux.set_proximo(self._topo)
            self._topo = aux
            return True
        return False
    # REMOVENDO O ELEMENTO DO TOP
    def remover(self):
        self._topo = self._topo.get_proximo()
        return True
    # RETORNANDO O TAMANHO DA PILHA
    def tamanho(self):
        count = 0
        if self._topo == None:
            return count
        else:
            aux = self._topo
            while aux.get_proximo() != None:
                aux = aux.get_proximo
                count += 1
            return count
    # RETORNANDO O ELEMENTO DO TOP
    def get_topo(self):
        return self._topo

##############
# CLASSE FILA:
##############
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