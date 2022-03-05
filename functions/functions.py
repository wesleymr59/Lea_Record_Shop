from database.database import Pedido

db_pedido = Pedido()

def realiza_pedido(pedido):
    print(pedido)
    db_pedido.insert_pedido(pedido)

def busca_estoque(nome_disco):
    estoque = db_pedido.select_pedido(nome_disco)
    print(estoque[0])
    return estoque[0]

def confere_estoque(estoque,valor_pedido,nome_disco):
    print('conferencia do estoque')
    print(estoque)
    print(valor_pedido)
    valor_novo_estoque = estoque - valor_pedido
    print(valor_novo_estoque)
    teste = db_pedido.update_pedido(valor_novo_estoque,nome_disco)
    print(teste)
