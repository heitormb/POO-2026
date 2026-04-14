import math

class Circulo:
    def __init__(self):
        self.__raio = 0.0  # atributo privado

    # Setter
    def set_raio(self, raio):
        self.__raio = raio

    # Getter
    def get_raio(self):
        return self.__raio

    # Calcular área
    def calc_area(self):
        return math.pi * self.__raio ** 2

    # Calcular circunferência
    def calc_circunferencia(self):
        return 2 * math.pi * self.__raio
    

c = Circulo()

c.set_raio(5.0)

print("Raio:", c.get_raio())
print("Área:", c.calc_area())
print("Circunferência:", c.calc_circunferencia())