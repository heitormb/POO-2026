class agua:
    def __init__(self, mes, ano, consumo):
        self.mes = mes
        self.ano = ano
        self.consumo = consumo
        self.conta = 0

    def calcular_conta(self):
        if self.consumo <= 10:
            self.conta = 38
        elif self.consumo <= 20:
            self.conta = 38 + (self.consumo - 10) * 5
        else:
            self.conta = 38 + (10 * 5) + (self.consumo - 20) * 6
        
        return self.conta

mes = input("Digite o mês: ")
ano = int(input("Digite o ano: "))
consumo = float(input("Digite o consumo de água em metros cubicos: "))

dados = agua(mes, ano, consumo)

conta = dados.calcular_conta()

print(f"mês:{dados.mes} ano:{dados.ano} consumo:{dados.consumo} valor a pagar:{conta:.2f}")