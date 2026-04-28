class Pais:
    def __init__(self, nome: str, populacao: int, area: float):
        self.set_nome(nome)
        self.set_populacao(populacao)
        self.set_area(area)

    def get_nome(self):
        return self._nome

    def get_populacao(self):
        return self._populacao

    def get_area(self):
        return self._area

    def set_nome(self, nome):
        self._nome = nome

    def set_populacao(self, populacao):
        self._populacao = populacao

    def set_area(self, area):
        self._area = float(area)

    def densidade(self):
        return self._populacao / self._area

    def __str__(self):
        return (f"País: {self._nome}\n"
                f"População: {self._populacao}\n"
                f"Área: {self._area:.2f} km²")


class PaisUI:
    @staticmethod
    def menu():
        print("\n--- MENU ---")
        print("1 - Calcular densidade demográfica")
        print("2 - Fim")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return 0

    @staticmethod
    def calculo():
        try:
            nome = input("Informe o nome do país: ")
            populacao = int(input("Informe a população: "))
            area = float(input("Informe a área (km²): "))

            pais = Pais(nome, populacao, area)

            print("\n--- Dados do País ---")
            print(pais)

            densidade = pais.densidade()
            print(f"Densidade demográfica: {densidade:.2f} hab/km²")

        except ValueError as e:
            print(f"Erro: {e}")

    @staticmethod
    def main():
        while True:
            opcao = PaisUI.menu()
            if opcao == 1:
                PaisUI.calculo()
            elif opcao == 2:
                print("Encerrando o programa...")
                break
            else:
                print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    PaisUI.main()