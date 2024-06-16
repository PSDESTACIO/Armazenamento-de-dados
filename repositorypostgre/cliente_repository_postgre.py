# Instale psycogp2 com 'pip install psycopg2-binary' para usar esse arquivo.
import psycopg2
from hashlib import sha256

class ClienteRepositoryPostgre:
    def __init__(self):
        # Essa senha (password) muda dependendo da sua senha que você colocou no seu banco de dados de exemplo.
        self.conn = psycopg2.connect(dbname="banco1",user="postgres", password="root", host="localhost",port="5432")
        self.cursor = self.conn.cursor()
        self.conn.autocommit = True

    # Tenta salvar os dados na base de dados.
    def save(self, cliente):
        try:
            hashed_password1 = sha256(cliente.senha.encode()).digest()
            hashed_password2 = sha256('$%.*'.encode()).digest()
            combined_hash = hashed_password1 + hashed_password2

            self.cursor.execute("INSERT INTO cliente (nome, email, senha) VALUES (%s, %s, %s)",(cliente.nome, cliente.email, combined_hash.hex()))
            self.conn.commit()
            return "Dados gravados no PostgreSQL."
        
        except Exception as error:
            return f"Error : {error}"
        
    # Método que printa todos os itens em clientes.
    def findAll(self):
        try:
            self.cursor.execute("select id, nome, email from cliente")
            rows = self.cursor.fetchall()

            for linha in rows:
                print(f"ID: {linha[0]}, Nome: {linha[1]}, Email: {linha[2]}, Senha: {linha[3]}")

        except Exception as error:
            print(f"Error : {error}")
             