from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, numero_conta, saldo = 0):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} efetuado! Seu novo saldo é R$ {self.saldo:.2f}.")

    @abstractmethod
    def sacar(self, valor):
        ...

    def __repr__(self):
        class_name = type(self).__name__
        atributos = f'({self.agencia!r}, {self.numero_conta!r}, {self.saldo!r})'
        return f'{class_name}{atributos}'
    
class ContaCorrente(Conta):
    def __init__(self, agencia, numero_conta, saldo = 0, limite_extra = 0):
        super().__init__(agencia, numero_conta, saldo)
        self.limite_extra = limite_extra

    def sacar(self, valor):
        if (self.saldo + self.limite_extra) - valor >= 0:
            self.saldo -= valor
            print(f"Saque de R$ {valor} efetuado! Seu novo saldo é R$ {self.saldo:.2f}.")
        else:
            print(f"Saldo insuficiente! Seu saldo é R$ {self.saldo:.2f}.")

    def detalhes(self):
        return f"A conta de número {self.numero_conta}, da agência {self.agencia}, "\
            f"tem o saldo R$ {(self.saldo):.2f}, além de R$ {(self.saldo + self.limite_extra):.2f} em limite extra restante."
    
    def __repr__(self):
        class_name = type(self).__name__
        atributos = f'({self.agencia!r}, {self.numero_conta!r}, {self.saldo!r}, {self.limite_extra!r})'
        return f'{class_name}{atributos}'

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo - valor >= 0:
            self.saldo -= valor
            print(f"Saque de R$ {valor} efetuado! Seu novo saldo é R$ {self.saldo:.2f}.")
        else:
            print(f"Saldo insuficiente. Seu saldo é R$ {self.saldo:.2f}.")

    def detalhes(self):
        return f"A conta de número {self.numero_conta}, da agência {self.agencia}, tem o saldo R$ {self.saldo:.2f}."
    
    def __repr__(self):
        class_name = type(self).__name__
        atributos = f'({self.agencia!r}, {self.numero_conta!r}, {self.saldo!r})'
        return f'{class_name}{atributos}'