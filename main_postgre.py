from model.cliente import Cliente
from repositorypostgre.cliente_repository_postgre import ClienteRepositoryPostgre


cliente1 = Cliente(nome="lu",email="lu@gmail.com")
cliente2 = Cliente(nome="italo",email="italo@gmail.com")

try:
    # Tenta salvar adicionar os clientes definidos acima na base de dados PostgreSQL.
    repository = ClienteRepositoryPostgre()
    msg = repository.save(cliente1)
    msg2 = repository.save(cliente2)

    # O método save retorna strings com o resultado do procedimento.
    print(f"{msg} , {msg2}")
    repository.findAll()

except Exception as error:
    print(f"Error : {error}")
