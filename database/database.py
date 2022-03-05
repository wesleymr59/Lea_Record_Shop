import psycopg2, os

class Database_Client():
    def setConnection(self):
        try:
            self.connection = psycopg2.connect(user=os.getenv("ENV_USER"),
                                        password=os.getenv("ENV_PASSWD"),
                                        host=os.getenv("ENV_HOST"),
                                        port=os.getenv("ENV_PORT"),
                                        database=os.getenv("ENV_DATABASE"))
            
            return self.connection

        except (Exception, psycopg2.Error) as error:
            return("Failed to connection", error)

    def insert_client(self,request_client:dict()):
        try:
            postgres_insert_query = f""" 
                                        INSERT INTO cliente (documento,nome_completo,data_nascimento,email,telefone,ativo)
                                        VALUES (
                                            '{request_client["documento"]}',
                                            '{request_client["nome_completo"]}',
                                            '{request_client["nascimento"]}',
                                            '{request_client["email"]}',
                                            '{request_client["telefone"]}',
                                            1);"""
            
            cursor = self.setConnection().cursor()
            cursor.execute(postgres_insert_query)
            self.connection.commit()
            count = cursor.rowcount
            cursor.close()
            return(f"{count} Record inserted successfully into client table")
        except (Exception, psycopg2.Error) as error:
            return("Failed to INSERT record into CLIENT table")

    def update_cliente(self, request_client:dict()):
        try:
            postgres_update_query =f""" update
                                            cliente 
                                        set 
                                            documento = '{request_client["documento"]}',
                                            data_nascimento = '{request_client["nascimento"]}',
                                            email = '{request_client["email"]}',
                                            telefone = '{request_client["telefone"]}'
                                        where
                                            nome_completo = '{request_client["nome"]}'"""

            cursor = self.setConnection().cursor()
            cursor.execute(postgres_update_query)
            self.connection.commit()
            count = cursor.rowcount
            cursor.close()
            return(f"{count} Record updated successfully into CLIENT table")
        except (Exception, psycopg2.Error) as error:
            return("Failed to UPDATE into CLIENT table", error)

    def select_client(self, request_client:dict()):
        try:
            postgres_select_query = f""" select * from cliente where nome_completo = {request_client["nome"]} """
            cursor = self.setConnection().cursor()
            cursor.execute(postgres_select_query)
            clients = cursor.fetchall()
            return clients
        except (Exception, psycopg2.Error) as error:
            return("Failed to SELECT into CLIENT table", error)

    def delete_client(self, request_client:dict()):
        try:
            postgres_delete_query = f""" UPDATE 
                                            cliente
                                        SET 
                                            ativo = 0
                                        WHERE
                                            nome_completo = '{request_client:dict()["nome"]}'
                                        AND
                                            documento = '{request_client:dict()["documento"]}'
                                        """
            cursor = self.setConnection().cursor()
            cursor.execute(postgres_delete_query)
            self.connection.commit()
            count = cursor.rowcount
            cursor.close()
            return(f"{count} Record updated successfully into CLIENT table")
        except (Exception, psycopg2.Error) as error:
            return("Failed to DELETE into CLIENT table", error)

class Database_Disc():

    def setConnection(self):
        try:
            self.connection = psycopg2.connect(user=os.getenv('ENV_USER'),
                                        password=os.getenv("ENV_PASSWD"),
                                        host=os.getenv("ENV_HOST"),
                                        port=os.getenv("ENV_PORT"),
                                        database=os.getenv("ENV_DATABASE"))
            
            return self.connection

        except (Exception, psycopg2.Error) as error:
            return("Failed to connection", error)

    def insert_disc(self,request_disc:dict()):
        try:
            postgres_insert_query = f""" 
                                        INSERT INTO discos (nome,artista,ano_lancamento,estilo,quantidade)
                                        VALUES (
                                            '{request_disc["nome"]}',
                                            '{request_disc["artista"]}',
                                            '{request_disc["ano_lancamento"]}',
                                            '{request_disc["estilo"]}',
                                            {request_disc["quantidade"]}
                                        );"""
            
            cursor = self.setConnection().cursor()
            cursor.execute(postgres_insert_query)
            self.connection.commit() 
            count = cursor.rowcount
            cursor.close()
            return(f"{count} Record inserted successfully into DISC table")
        except (Exception, psycopg2.Error) as error:
            return("Failed to INSERT into DISC table", error)

    def update_disc(self, request_disc:dict()):
        try:
            postgres_update_query =f""" update
                                            discos
                                        set
                                            artista = '{request_disc["artista"]}',
                                            ano_lancamento = '{request_disc["ano_lancamento"]}',
                                            estilo = '{request_disc["estilo"]}',
                                            quantidade = {request_disc["quantidade"]}
                                        where
                                            nome = '{request_disc["nome"]}'"""

            cursor = self.setConnection().cursor()
            cursor.execute(postgres_update_query)
            self.connection.commit()
            count = cursor.rowcount
            cursor.close()
            return(f"{count} Record updated successfully into DISC table")
        except (Exception, psycopg2.Error) as error:
            return("Failed to UPDATE into DISC table", error)

    def select_disc(self,request_disc:dict()):
        try:
            postgres_select_query = f""" select * 
                                        from 
                                            discos 
                                        where 
                                            nome = '{request_disc["nome"]}' """
            cursor = self.setConnection().cursor()
            cursor.execute(postgres_select_query)
            clients = cursor.fetchall()
            return clients
        except (Exception, psycopg2.Error) as error:
            return("Failed to SELECT into DISC table", error)
    
    def delete_disc(self, request_disc:dict()):
        try:
            postgres_delete_query = f""" UPDATE 
                                            discos
                                        SET 
                                            quantidade = 0
                                        WHERE
                                            nome = '{request_disc["nome"]}'
                                        AND
                                            artista = '{request_disc["artista"]}'
                                        """
            cursor = self.setConnection().cursor()
            cursor.execute(postgres_delete_query)
            self.connection.commit()
            count = cursor.rowcount
            cursor.close()
            return(f"{count} Record updated successfully into CLIENT table")
        except (Exception, psycopg2.Error) as error:
            return("Failed to DELETE into DISC table", error)

class Pedido():
    def setConnection(self):
        try:
            self.connection = psycopg2.connect(user=os.getenv('ENV_USER'),
                                        password=os.getenv("ENV_PASSWD"),
                                        host=os.getenv("ENV_HOST"),
                                        port=os.getenv("ENV_PORT"),
                                        database=os.getenv("ENV_DATABASE"))
            
            return self.connection

        except (Exception, psycopg2.Error) as error:
            return("Failed to connection", error)

    def insert_purchase(self, request_disc:dict()):
        try: 
            postgres_insert_query = f""" 
                                        INSERT INTO pedido (cliente,disco,quantidade,data_pedido)
                                        VALUES (
                                            '{request_disc["nome_cliente"]}',
                                            '{request_disc["nome_disco"]}',
                                            '{request_disc["quantidade"]}',
                                            '{request_disc["data_pedido"]}'
                                        );"""
            
            cursor = self.setConnection().cursor()
            cursor.execute(postgres_insert_query)
            self.connection.commit() 
            count = cursor.rowcount
            cursor.close()
            return(f"{count} Record inserted successfully into PEDIDO table")
        except (Exception, psycopg2.Error) as error:
            return("Failed to INSERT into PEDIDO table", error)

    def select_pedido(self,request_pedido:str):
        try:
            postgres_select_query = f""" select quantidade 
                                        from 
                                            discos 
                                        where 
                                            nome = '{request_pedido}' """
            cursor = self.setConnection().cursor()
            cursor.execute(postgres_select_query)
            clients = cursor.fetchone()
            return clients
        except (Exception, psycopg2.Error) as error:
            return("Failed to SELECT into PEDIDO table", error)
    
    def update_pedido(self, quantidade:int,nome:str()):
        try:
            postgres_delete_query = f""" UPDATE 
                                            discos
                                        SET 
                                            quantidade = {quantidade}
                                        WHERE
                                            nome = '{nome}'
                                        """
            cursor = self.setConnection().cursor()
            cursor.execute(postgres_delete_query)
            self.connection.commit()
            count = cursor.rowcount
            cursor.close()
            return(f"pedido efetuado com sucesso")
        except (Exception, psycopg2.Error) as error:
            return("Failed to UPDATE into PEDIDO table", error)
    
    def select_client(self, request_client:dict()):
        try:
            postgres_select_query = f"""SELECT * FROM pedido
                                        WHERE
                                            data_pedido  
                                        BETWEEN '{request_client["date_init"]}' AND '{request_client["date_end"]}' """
            cursor = self.setConnection().cursor()
            cursor.execute(postgres_select_query)
            clients = cursor.fetchall()
            return clients
        except (Exception, psycopg2.Error) as error:
            return("Failed to SELECT into Pedido table", error)