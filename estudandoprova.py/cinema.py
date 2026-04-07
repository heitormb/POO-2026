class Cinema():
    def __init__(self, dia, horario):
        self.dia = dia
        self.horario = horario

    def calcular_valor(self):
        if self.dia == "segunda":
            valor = 16
        elif self.dia == "terça":
            valor = 16
        elif self.dia == "quinta":
            valor = 16
        elif self.dia == "quarta":
            valor = 8
        elif self.dia == "sexta":
            valor = 20
        elif self.dia == "sábado":
            valor = 20
        elif self.dia == "domingo":
            valor = 20

        if self.horario in range(17, 25):
            valor = valor + valor/2

        return valor


dia = input("digite o dia do filme: ")
horario = int(input("digite o horário do filme: "))

filme = Cinema(dia, horario)
custo = filme.calcular_valor()
print(custo)