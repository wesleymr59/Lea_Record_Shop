from datetime import date
from functions.functions import realiza_pedido,busca_estoque,confere_estoque
from fastapi import FastAPI
from pydantic import BaseModel
from database.database import Database_Client, Database_Disc

app = FastAPI()
db_cli = Database_Client()
db_disc = Database_Disc()

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

class pedido(BaseModel):
    nome_cliente:str
    nome_disco:str
    quantidade:int
    data_pedido:date
#Rotas de pedido


#Fim rotas de pedido

#Rotas de pedido
@app.post("/pedido")
async def insert_pedido(pedido:pedido) -> str:
    pedido = pedido.dict()
    realiza_pedido(pedido)
    estoque = busca_estoque(pedido['nome_disco'])
    confere_estoque(estoque,pedido['quantidade'],pedido['nome_disco'])
    return "ok"


#Rotas relacionadas aos discos

@app.get("/discs/select")
def select_disc(discs:discs):
    discs = discs.dict()
    select_clientes = db_disc.select_disc(discs)
    return select_clientes


@app.post("/discs/insert")
async def insert_disc(discs:discs) -> str:
    discs = discs.dict()
    insert_banco_cliente = db_disc.insert_disc(discs)
    return insert_banco_cliente


@app.put("/discs/update")
async def update_disc(discs:discs)-> str:
    discs = discs.dict()
    update_banco_disc = db_disc.update_disc(discs)
    return update_banco_disc


@app.delete("/discs/delete")
def delete_discs(discs:discs)-> str:
    discs = discs.dict()
    delete_banco_disc = db_disc.delete_disc(discs)
    return delete_banco_disc

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
    insert_banco_cliente = db_cli.insert_client(client)
    return insert_banco_cliente


@app.put("/cliente/update")
async def insert_client(client:client)-> str:
    client = client.dict()
    update_banco_cliente = db_cli.update_cliente(client["documento"],client["nome"],client["nascimento"],client["email"],client["telefone"])
    return update_banco_cliente


@app.delete("/cliente/delete")
def delete_client(client:client)-> str:
    client = client.dict()
    delete_banco_cliente = db_cli.delete_client(client)
    return delete_banco_cliente

#Fim das rotas relacionadas aos clientes