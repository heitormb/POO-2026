class Pais:
    def __init__(self, nome, populacao, area):
        self.nome = nome
        self.populacao = populacao
        self.area = area

    def calcular_densidade(self):
        return self.populacao / self.area

ps = []

for i in range(1, 11):
    nome = input("Digite o nome do país: ")
    populacao = int(input("Digite sua população: "))
    area = float(input("Digite a área em km2: "))
    
    p = Pais(nome, populacao, area)
    ps.append(p)


maior = ps[0]

for pais in ps:
    if pais.calcular_densidade() > maior.calcular_densidade():
        maior = pais


print(f"País com maior densidade: {maior.nome}")
print(f"Densidade: {maior.calcular_densidade():.2f} hab/km²")