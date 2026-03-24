class Triangulo:
    def __init__(self):
        self.b = 0
        self.h = 0
    def calc_area(self):
        return self.b * self.h / 2

x = Triangulo()
print(x.b, x.h)
x.b = float(input("Informe a base do triângulo\n"))
x.h = float(input("Informe a altura do triângulo\n"))
print(x.b, x.h)
a = x.calc_area()
print(f"A área do triângulo é {a:.2f}")

y = Triangulo()
print(y.b, y.h)
y.b = float(input("Informe a base do triângulo\n"))
y.h = float(input("Informe a altura do triângulo\n"))
print(y.b, y.h)
a = y.calc_area()
print(f"A área do triângulo é {a:.2f}")