from list_de_compras import ListaCompras, menu_add_item, menu_remover_item, imprimir_lista
from carrinho import Carrinho, add_carrinho, remover_item_carrinho, imprimir_carrinho
from caixa import Caixa, imprimir_caixa

from utils import clean_screen


opcao = 0
lista = ListaCompras()
carrinho = Carrinho()
caixa = Caixa()

# menu lista
while opcao != 4:
    clean_screen()
    print('\t╔════════════════════════════════╗')
    print('\t║ 1º: Fazendo a lista de compras ║')
    print('\t╠════════════════════════════════╣')
    print('\t║ Opção 1 »» adionar item        ║')
    print('\t║ Opção 2 »» remover item        ║')
    print('\t║ Opção 3 »» ver a lista         ║')
    print('\t║ Opção 4 »» ir para o mercado   ║')
    print('\t╚════════════════════════════════╝')

    opcao = int(input('\n»sua opção: '))
    clean_screen()

    if opcao < 1 or opcao > 4:
        print('\n\t»opção inválida!!')
        opcao = int(input('\t»selecione uma opção novamente: '))

    elif opcao == 1:
        menu_add_item(lista)

    elif opcao == 2:
        menu_remover_item(lista)

    elif opcao == 3:
        imprimir_lista(lista)
        input('\n\n\n»precione enter para continuar...')

    elif opcao == 4:
        if lista.vazia():
            print('\n\t»»lista vazia, tente adicionar itens para finalizar.')
            item = input('\n\t»»insira seu item no carrinho: ')
            menu_add_item(lista)
            opcao = 1
        else:
            print('\n\t»»lista finalizada, se direcione ao supermercado!')

# menu pilha
while not lista.vazia():
    clean_screen()
    print('\t╔═════════════════════════════════════╗')
    print('\t║ 2º: Colocando itens no carrinho     ║')
    print('\t╠═════════════════════════════════════╣')
    print('\t║ Opção 1 »» adionar item             ║')
    print('\t║ Opção 2 »» remover item             ║')
    print('\t║ Opção 3 »» exibir itens do carrinho ║')
    print('\t╚═════════════════════════════════════╝')
    
    opcao = int(input('\n»sua opção: '))
    clean_screen()

    if opcao < 1 or opcao > 3:
        print('\n\t»opção inválida!!')
        opcao = int(input('\t»selecione uma opção novamente: '))

    elif opcao == 1:
        add_carrinho(lista, carrinho)

    elif opcao == 2:
        remover_item_carrinho(carrinho)

    elif opcao == 3:
        imprimir_carrinho(carrinho)
        input('\n\n\n»precione enter para continuar...')


# menu fila
while not carrinho.vazio() or not caixa.vazio():
    clean_screen()
    print('\t╔════════════════════════════════════════════╗')
    print('\t║ 3º: Passando no caixa os itens do carrinho ║')
    print('\t╚════════════════════════════════════════════╝')
    print('\t║ Opção 1 »» botar item                      ║')
    print('\t║ Opção 2 »» passar/comprar item             ║')
    print('\t║ Opção 3 »» exibir itens no caixa           ║')
    print('\t╚════════════════════════════════════════════╝')
    imprimir_carrinho(carrinho)
    opcao = int(input('\n»sua opção: '))

    clean_screen()
    if opcao < 1 or opcao > 3:
        print('\n\t»opção inválida!!')
        opcao = int(input('\t»selecione uma opção novamente: '))

    elif opcao == 1:
        if carrinho.vazio():
            print('\n\t»opção inválida!!')
            print('\t»Carrinho Vazio')
        else:
            aux = carrinho.remover_item()
            caixa.adicionar_item(aux)
            print('\n\t»»item {aux} foi colocado no caixa!'.format(aux=aux))
            input('\n\n\n»precione enter para continuar...')

    elif opcao == 2:
        if caixa.vazio():
            print('\n\t»opção inválida!!')
            print('\t»Caixa Vazio')
        else:
            aux = caixa.remover()
            print('\n\t»»item {aux} foi colocado no caixa!'.format(aux=aux))
            input('\n\n\n»precione enter para continuar...')

    elif opcao == 3:
        imprimir_caixa(carrinho)
    
    input('\n\n\n»precione enter para continuar...')

clean_screen()

print("Volte Sempre!")
