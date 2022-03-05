from database.database import Pedido

db_purchase = Pedido()

def accomplish_purchase(purchase):
    db_purchase.insert_purchase(purchase)

def search_stock(name_disc):
    stock = db_purchase.select_pedido(name_disc)
    if stock[0] == 0:
        return True
    else:
        return stock[0]

def check_stock(stock,order_value,name_disc):
    if order_value > stock:
        return "valor do pedido maior que o estoque"   
    else:
        value_new_stock = stock - order_value
        purchase = db_purchase.update_pedido(value_new_stock,name_disc)
        return purchase

def select_date_purchase(order_date):
    order_made = db_purchase.select_pedido(order_date)
    return order_made