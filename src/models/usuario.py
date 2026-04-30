class Usuario:
    def __init__(self, nome, email):
        self.isValid(nome, email)
        self.nome = nome
        self.email = email
    
    def isValid(self, nome, email):
        if "@" not in email:
            raise ValueError