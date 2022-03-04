from datetime import date
from fastapi import FastAPI
from pydantic import BaseModel
from database.database import Database

app = FastAPI()
db = Database()

class client(BaseModel):
    documento:str
    nome:str
    nascimento:date
    email:str
    telefone:str


@app.get("/")
def read_user_me():
    return "api conectada"


@app.get("cliente/select")
def select_cliente():
    select_clientes = db.select_client()
    return select_clientes


@app.post("/cliente/insert")
async def insert_cliente(client:client):
    client = client.dict()
    insert_banco_cliente = db.insert_client(client["documento"],client["nome"],client["nascimento"],client["email"],client["telefone"])
    return insert_banco_cliente


@app.put("/cliente/update")
async def insert_cliente(client:client):
    client = client.dict()
    update_banco_cliente = db.update_cliente(client["documento"],client["nome"],client["nascimento"],client["email"],client["telefone"])
    return update_banco_cliente


@app.delete("cliente/delete")
def delete_cliente(client:client):
    client = client.dict()
    delete_banco_cliente = db.delete_client(client["documento"],client["nome"])
    return delete_banco_cliente