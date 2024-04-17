class Cliente:
    def __init__(self,id=None,nome=None,email=None):
        self.id = id
        self.nome = nome
        self.email = email
    
    def __str__(self):
        return f"id={self.id}, nome={self.nome}, email={self.email}"
    
    def __dict__(self):
        return  {
            'id':self.id,
            'nome':self.nome,
            'email':self.email
        }
    
    def toString(self):
        return f"{self.id}, {self.nome}, {self.email}"
