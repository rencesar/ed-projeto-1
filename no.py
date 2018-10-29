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
