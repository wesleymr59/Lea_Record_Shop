import re
from datetime import date
from functions.functions import accomplish_purchase,search_stock,check_stock,select_date_purchase
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from database.database import Database_Client, Database_Disc

app = FastAPI()
db_cli = Database_Client()
db_disc = Database_Disc()

regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
regex_telefone = r'^\(?(?:[14689][1-9]|2[12478]|3[1234578]|5[1345]|7[134579])\)? ?(?:[2-8]|9[1-9])[0-9]{3}\-?[0-9]{4}$'
#Base model para os requests
class client(BaseModel):
    documento:str
    nome_completo:str
    nascimento:date
    email:str
    telefone:str

class discs(BaseModel):
    nome:str
    artista:str
    ano_lancamento:date
    estilo:str
    quantidade:int

class purchase(BaseModel):
    nome_cliente:str
    nome_disco:str
    quantidade:int
    data_pedido:date

class date_purchase(BaseModel):
    date_init:date
    date_end:date


#Rotas de pedido
@app.post("/pedido")
async def insert_pedido(purchase:purchase) -> str:
    purchase = purchase.dict()   
    stock = search_stock(purchase['nome_disco'])
    if stock == True:
        return HTTPException(status_code=400, detail="discos esgotados")
    else:
        print("ta chegando aqui")
        accomplish_purchase(purchase)
        check = check_stock(stock,purchase['quantidade'],purchase['nome_disco'])
        return check

@app.get("/select/pedido")
async def insert_pedido(date_purchase:date_purchase) -> str:
    date_purchase = date_purchase.dict()
    select_date_purchase(date_purchase)

#Fim rotas de pedido

#Rotas relacionadas aos discos

@app.get("/discs/select")
def select_disc(discs:discs)-> str:
    discs = discs.dict()
    select_clientes = db_disc.select_disc(discs)
    return select_clientes


@app.post("/discs/insert")
async def insert_disc(discs:discs) -> str:
    discs = discs.dict()
    insert_customer_bank = db_disc.insert_disc(discs)
    return insert_customer_bank


@app.put("/discs/update")
async def update_disc(discs:discs)-> str:
    discs = discs.dict()
    update_database_disc = db_disc.update_disc(discs)
    return update_database_disc


@app.delete("/discs/delete")
def delete_discs(discs:discs)-> str:
    discs = discs.dict()
    delete_database_disc = db_disc.delete_disc(discs)
    return delete_database_disc

#Fim das rotas relacionadas aos discos


#Rotas relacionadas aos clientes

@app.get("/")
def read_user_me():
    return "api conectada"


@app.get("/cliente/select")
def select_client():
    select_clientes = db_cli.select_client()
    return select_clientes


@app.post("/cliente/insert")
async def insert_client(client:client) -> str:
    client = client.dict()
    if re.fullmatch(regex_email, client['email']) and re.fullmatch(regex_telefone, client['telefone']) :
        insert_database_cliente = db_cli.insert_client(client)
        if insert_database_cliente!=None:
            return insert_database_cliente
        return insert_database_cliente
    else:
        return "email ou telefone invalido"

@app.put("/cliente/update")
async def insert_client(client:client)-> str:
    client = client.dict()
    update_database_cliente = db_cli.update_cliente(client["documento"],client["nome"],client["nascimento"],client["email"],client["telefone"])
    return update_database_cliente


@app.delete("/cliente/delete")
def delete_client(client:client)-> str:
    client = client.dict()
    delete_database_cliente = db_cli.delete_client(client)
    return delete_database_cliente

#Fim das rotas relacionadas aos clientes