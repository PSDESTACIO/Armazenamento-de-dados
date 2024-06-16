class Cliente:
    def __init__(self, id=None, nome=None, email=None, senha = None):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
    
    def __str__(self):
        return f"id={self.id}, nome={self.nome}, email={self.email}, senha={self.senha}"
    
    def __dict__(self):
        return  {
            'id':self.id,
            'nome':self.nome,
            'email':self.email,
            'senha':self.senha
        }
    
    def toString(self):
        return f"{self.id}, {self.nome}, {self.email}, {self.senha}"
