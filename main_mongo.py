from model.cliente import Cliente
from repositorymongo.cliente_repository_mongo import ClienteRepositoryMongo

try:
    cliente1 = Cliente(nome='ana',email='ana@gmail.com')
    cliente2 = Cliente(nome='italo',email='italo@gmail.com')
    mongo_repo = ClienteRepositoryMongo()
    mongo_repo.save(cliente1)
    mongo_repo.save(cliente2)

    lista_clientes =  mongo_repo.findAll()
    for cliente in lista_clientes:
        print(cliente)
    print("gravamos e listamos do MongoDb")

except Exception as error:
    print(f"{error}")







