class ContaBancaria:
    def __init__(self):
        self._titular = ""
        self._numero = ""
        self._saldo = 0.0

    def set_titular(self, nome):
        self._titular = nome

    def set_numero(self, numero):
        self._numero = numero

    def set_saldo(self, saldo):
        if saldo >= 0:
            self._saldo = saldo
        else:
            raise ValueError("Saldo não pode ser negativo.")

    def get_titular(self):
        return self._titular

    def get_numero(self):
        return self._numero

    def get_saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
        else:
            raise ValueError("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("Valor de saque inválido.")
        if valor > self._saldo:
            raise ValueError("Saldo insuficiente.")
        self._saldo -= valor


if __name__ == "__main__":
    conta = ContaBancaria()

    conta.set_titular("João Silva")
    conta.set_numero("12345-6")
    conta.set_saldo(1000.0)

    print("Titular:", conta.get_titular())
    print("Conta:", conta.get_numero())
    print("Saldo inicial:", conta.get_saldo())

    conta.depositar(500)
    print("Após depósito:", conta.get_saldo())

    conta.sacar(300)
    print("Após saque:", conta.get_saldo())