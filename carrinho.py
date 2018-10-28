from library import No, Pilha, Fila, ListaEnc

def add_carrinho(lista, pilha):
    while lista.vazia():
        aux = lista.get_cauda()
        pilha.add(aux)
        lista.remover_fim()

def remover_carrinho(pilha, fila):
    while pilha.vazia():
        aux = pilha.get_topo()

