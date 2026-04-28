class Viagem:
    def __init__(self, destino: str, distancia: float, litros: float):
        self.set_destino(destino)
        self.set_distancia(distancia)
        self.set_litros(litros)

    def get_destino(self):
        return self._destino

    def get_distancia(self):
        return self._distancia

    def get_litros(self):
        return self._litros

    def set_destino(self, destino):
        self._destino = destino

    def set_distancia(self, distancia):
        self._distancia = float(distancia)

    def set_litros(self, litros):
        self._litros = float(litros)

    def consumo(self):
        return self._distancia / self._litros

    def __str__(self):
        return (f"Destino: {self._destino}\n"
                f"Distância: {self._distancia:.2f} km\n"
                f"Combustível: {self._litros:.2f} L")


class ViagemUI:
    @staticmethod
    def menu():
        print("\n--- MENU ---")
        print("1 - Calcular consumo")
        print("2 - Fim")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return 0

    @staticmethod
    def calculo():
        try:
            destino = input("Informe o destino: ")
            distancia = float(input("Informe a distância (km): "))
            litros = float(input("Informe o combustível gasto (L): "))

            viagem = Viagem(destino, distancia, litros)

            print("\n--- Dados da Viagem ---")
            print(viagem)

            consumo = viagem.consumo()
            print(f"Consumo médio: {consumo:.2f} km/L")

        except ValueError as e:
            print(f"Erro: {e}")

    @staticmethod
    def main():
        while True:
            opcao = ViagemUI.menu()
            if opcao == 1:
                ViagemUI.calculo()
            elif opcao == 2:
                print("Encerrando o programa...")
                break
            else:
                print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    ViagemUI.main()