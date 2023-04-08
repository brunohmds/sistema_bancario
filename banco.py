import pessoa, contas

#def __init__ (self, agencias, clientes, contas):
class Banco:
    def __init__(
        self,
        agencias: list[int] | None = None,
        clientes: list[pessoa.Pessoa] | None = None,
        contas: list[contas.Conta] | None = None):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def autenticar(self, cliente, conta):
        if self._checa_agencia(conta) and self._checa_cliente(cliente) and self._checa_conta(conta) and self._checa_conta_do_cliente (cliente, conta) == True:
            return True

    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            return True
        return False
                
    def _checa_conta(self, conta):
        if conta in self.contas:
            return True
        return False
    
    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            return True
        return False
    
    def _checa_conta_do_cliente(self, cliente, conta):
        if conta is cliente.conta:
            return True
        return False

    def __repr__(self):
        class_name = type(self).__name__
        atributos = f"({self.agencias!r}, {self.clientes!r}, {self.contas!r})"
        return f"{class_name}{atributos}"
    
if __name__ == '__main__':    
    cliente1 = pessoa.Cliente("Bruno", 29)
    conta1 = contas.ContaCorrente(111, 222, 0, 0)
    cliente1.conta = conta1

    cliente2 = pessoa.Cliente("Brenda", 29)
    conta2 = contas.ContaPoupanca(112, 223, 100)
    cliente2.conta = conta2

    banco1 = Banco()   
    banco1.clientes.append(cliente1)
    banco1.clientes.append(cliente2)

    banco1.contas.append(conta1)
    banco1.contas.append(conta2)

    banco1.agencias.append(111)
    banco1.agencias.append(222)

    if banco1.autenticar(cliente1, conta1):
        cliente1.conta.depositar(10)
        print(cliente1.conta)
