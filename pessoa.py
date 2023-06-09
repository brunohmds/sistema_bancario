class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome
        
    @property
    def idade(self):
        return self._idade
    
    def __repr__(self):
        class_name = type(self).__name__
        atributos = f'({self.nome!r}, {self.idade!r})'
        return f'{class_name}{atributos}' 
        
        
class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self._conta = None

    @property
    def conta(self):
        return self._conta
    
    @conta.setter
    def conta(self, conta):
        self._conta = conta
