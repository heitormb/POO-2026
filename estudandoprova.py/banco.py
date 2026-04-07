class Banco:
    def __init__(self, titular, numero, saldo, saque, deposito):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
        self.saque = saque
        self.deposito = deposito

    def sacar_depositar(self):
        self.valor_final = self.saldo + self.deposito - self.saque
        return self.valor_final


titular = input("Digite o nome do titular: ")
numero = input("digite o seu número da conta: ")
saldo = float(input("digite o seu saldo: "))
saque = float(input("Digite qual o valor que deseja sacar: "))
deposito = float(input("Digite o valor que deseja depositar: "))

conta = Banco(titular, numero, saldo, saque, deposito)

custo = conta.sacar_depositar()
print(custo)