class Pais:
    def __init__(self, nome, populacao, area):
        self.nome = nome
        self.populacao = populacao
        self.area = area

    def calcular_densidade(self):
        return self.populacao / self.area

nome = input("Digite o nome do país: ")
populacao = int(input("Digite sua população: "))
area = float(input("Digite a área em km2: "))

pais = Pais(nome, populacao, area)

densidade = pais.calcular_densidade()

print(f"A densidade demográfica do {pais.nome} é de {densidade:.2f} hab/km2")