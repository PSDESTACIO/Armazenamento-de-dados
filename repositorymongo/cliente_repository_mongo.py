from pymongo import MongoClient
from bson import ObjectId

class ClienteRepositoryMongo:
    def __init__(self):
        client = MongoClient('mongodb://localhost:27017/banconp')
        self.db = client['banconp']
        self.collection = self.db['cliente']
    
    def save(self, user):
        user_id= self.collection.insert_one({'nome':user.nome,'email':user.email})
        return str(user_id)
    
    def findAll(self):
        return list(self.collection.find({},{'_id':1,'nome':1,'email':1}))
