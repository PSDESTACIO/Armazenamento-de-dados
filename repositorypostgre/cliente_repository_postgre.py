import psycopg2

class ClienteRepositoryPostgre:
    def __init__(self):
        self.conn = psycopg2.connect(dbname="banco1",user="postgres", password="root1", host="localhost",port="5432")
        self.cursor = self.conn.cursor()
        self.conn.autocommit = True
    def save(self, cliente):
        cursor = None
        try:
            self.cursor.execute("insert into cliente (nome,email) values (%s,%s) ",(cliente.nome, cliente.email))
            self.conn.commit()
            return "dados gravados no postgres"
        except Exception as error:
            return f"Error : {error}"
        
    
    def findAll(self):
        cursor = None
        try:
            self.cursor.execute("select id, nome, email from cliente")
            rows = self.cursor.fetchall()
            for linha in rows:
                print(f"ID: {linha[0]}, Nome: {linha[1]}, Email: {linha[2]}")
        except Exception as error:
            print(f"Error :{error}")
 
             