from model.cliente import Cliente
from repositorypostgre.cliente_repository_postgre import ClienteRepositoryPostgre


cliente1 = Cliente(nome="lu",email="lu@gmail.com")
cliente2 = Cliente(nome="italo",email="italo@gmail.com")
try:
    repository = ClienteRepositoryPostgre()
    msg = repository.save(cliente1)
    msg2 = repository.save(cliente2)
    print(f"{msg} , {msg2}")
    repository.findAll()
except Exception as error:
    print(f" Error : {error}")


