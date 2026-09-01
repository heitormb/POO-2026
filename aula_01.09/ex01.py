class Triangulo:
    def __init__(self):
        self.b = 0
        self.h = 0
    def area(self):
        return self.b * self.h / 2
    def __str__(self):
        return f"Triângulo com base = {self.b} e altura = {self.h}"

class UI:
    def main():
        x = Triangulo()
        x.b = 10
        x.h = 20

        y = Triangulo()

        z = x
        z.b = 30
        z.h = 40

        print(x, x.b, x.h, x.area())
        print(y, y.b, y.h)

        l = [Triangulo(), x]
        l[1].b = 50
        l[1].h = 60
        print(x, x.b, x.h, x.area())


UI.main()