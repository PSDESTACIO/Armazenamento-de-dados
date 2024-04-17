# criei o banco e entrei no banco
> use banconp
# criando nao inseri o _id ... 
> db.cliente.insert({"nome":"belem","email":"belem@gmail.com"});
WriteResult({ "nInserted" : 1 })
 
# inseri somente o nome e o email
> db.cliente.find().pretty();
{
        "_id" : ObjectId("661be76a0fbfd11e55485ebd"),
        "nome" : "belem",
        "email" : "belem@gmail.com"
}
> db.cliente.find();
{ "_id" : ObjectId("661be76a0fbfd11e55485ebd"), "nome" : "belem", "email" : "belem@gmail.com" }
# mostrar
> db
banconp
> show collections;
cliente

db.cliente.insert({"nome":"jose","email":"jose@gmail.com"});

### ObjectId("cliente") ... relacionar

db.cliente.find({"nome":"jose"});
{ "_id" : ObjectId("661be8650fbfd11e55485ebe"), "nome" : "jose", "email" : "jose@gmail.com" }

## mostra os dados no mongo
db.cliente.find().pretty();


## infra mongo
## criar index

db.cliente.createIndex({email:1},{unique:true});