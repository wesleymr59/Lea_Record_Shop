import psycopg2

class Database():
    def setConnection(self):
        try:
            self.connection = psycopg2.connect(user="postgres",
                                        password="admin",
                                        host="192.168.86.75",
                                        port="5432",
                                        database="postgres")
            
            return self.connection

        except (Exception, psycopg2.Error) as error:
            print("Failed to insert record into mobile table", error)

    def insert_client(self,documento, nome, nascimento, email, telefone):
        postgres_insert_query = """ 
                                    INSERT INTO public.cliente (documento,nome_completo,data_nascimento,email,telefone,ativo)
	                                VALUES (%s,%s,%s,%s,%s,1);"""
        record_to_insert = (documento, nome, nascimento, email, telefone)
        cursor = self.setConnection().cursor()
        cursor.execute(postgres_insert_query, record_to_insert)
        self.connection.commit()
        count = cursor.rowcount
        cursor.close()
        return(f"{count}Record inserted successfully into client table")

    def update_cliente(self, documento, nome, nascimento, email, telefone):
        postgres_update_query =f""" update
                                        cliente 
                                    set 
                                        documento = '{documento}',
                                        data_nascimento = '{nascimento}',
                                        email = '{email}',
                                        telefone = '{telefone}'
                                    where
                                        nome_completo = '{nome}'"""

        cursor = self.setConnection().cursor()
        cursor.execute(postgres_update_query)
        self.connection.commit()
        count = cursor.rowcount
        cursor.close()
        return(f"{count}Record updated successfully into client table")


    def select_client(self):
        postgres_select_query = """ select * from cliente c where nome_completo = 'wesley marques' """
        cursor = self.setConnection().cursor()
        cursor.execute(postgres_select_query)
        clients = cursor.fetchall()
        return clients


    def delete_client(self, nome:str(), documento:str()):
        postgres_delete_query = f""" UPDATE 
                                        cliente
                                    SET 
                                        ativo = 0
                                    WHERE
                                        nome_completo = '{nome}'
                                    AND
                                        documento = '{documento}'
                                    """
        cursor = self.setConnection().cursor()
        cursor.execute(postgres_delete_query)
        self.connection.commit()
        count = cursor.rowcount
        cursor.close()
        return(f"{count}Record updated successfully into client table")