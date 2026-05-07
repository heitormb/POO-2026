class Time:
    def __init__(self, i: int, n: str, e: str):
        self.__id = i
        self.__nome = n
        self.__estado = e

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_estado(self):
        return self.__estado

    def set_nome(self, nome):
        self.__nome = nome

    def set_estado(self, estado):
        self.__estado = estado

    def ToString(self):
        return f"ID: {self.__id} | Nome: {self.__nome} | Estado: {self.__estado}"


class Jogador:
    def __init__(self, i: int, it: int, n: str, v: int):
        self.__id = i
        self.__idTime = it
        self.__nome = n
        self.__camisa = v

    def get_id(self):
        return self.__id

    def get_idTime(self):
        return self.__idTime

    def get_nome(self):
        return self.__nome

    def get_camisa(self):
        return self.__camisa

    def set_idTime(self, idTime):
        self.__idTime = idTime

    def set_nome(self, nome):
        self.__nome = nome

    def set_camisa(self, camisa):
        self.__camisa = camisa

    def ToString(self):
        return (
            f"ID: {self.__id} | "
            f"Nome: {self.__nome} | "
            f"Camisa: {self.__camisa} | "
            f"Time ID: {self.__idTime}"
        )


class UI:
    times = []
    jogadores = []


    @staticmethod
    def inserir_time():
        print("\n=== INSERIR TIME ===")

        id_time = int(input("ID do time: "))
        nome = input("Nome do time: ")
        estado = input("Estado: ")

        time = Time(id_time, nome, estado)
        UI.times.append(time)

        print("Time cadastrado com sucesso!")

    @staticmethod
    def listar_time():
        print("\n=== LISTA DE TIMES ===")

        if len(UI.times) == 0:
            print("Nenhum time cadastrado.")
            return

        for t in UI.times:
            print(t.ToString())

    @staticmethod
    def atualizar_time():
        print("\n=== ATUALIZAR TIME ===")

        id_time = int(input("Informe o ID do time: "))

        for t in UI.times:
            if t.get_id() == id_time:
                novo_nome = input("Novo nome: ")
                novo_estado = input("Novo estado: ")

                t.set_nome(novo_nome)
                t.set_estado(novo_estado)

                print("Time atualizado!")
                return

        print("Time não encontrado.")

    @staticmethod
    def excluir_time():
        print("\n=== EXCLUIR TIME ===")

        id_time = int(input("Informe o ID do time: "))

        for t in UI.times:
            if t.get_id() == id_time:

                # Remove jogadores do time
                UI.jogadores = [
                    j for j in UI.jogadores
                    if j.get_idTime() != id_time
                ]

                UI.times.remove(t)

                print("Time removido!")
                return

        print("Time não encontrado.")

    @staticmethod
    def inserir_jogador():
        print("\n=== INSERIR JOGADOR ===")

        id_jogador = int(input("ID do jogador: "))
        id_time = int(input("ID do time: "))
        nome = input("Nome do jogador: ")
        camisa = int(input("Número da camisa: "))

        time_existe = False

        for t in UI.times:
            if t.get_id() == id_time:
                time_existe = True
                break

        if not time_existe:
            print("Time não encontrado.")
            return

        jogador = Jogador(id_jogador, id_time, nome, camisa)
        UI.jogadores.append(jogador)

        print("Jogador cadastrado!")

    @staticmethod
    def listar_jogador():
        print("\n=== LISTA DE JOGADORES ===")

        if len(UI.jogadores) == 0:
            print("Nenhum jogador cadastrado.")
            return

        for j in UI.jogadores:
            print(j.ToString())

    @staticmethod
    def editar_jogador():
        print("\n=== EDITAR JOGADOR ===")

        id_jogador = int(input("Informe o ID do jogador: "))

        for j in UI.jogadores:
            if j.get_id() == id_jogador:

                novo_nome = input("Novo nome: ")
                nova_camisa = int(input("Novo número da camisa: "))

                j.set_nome(novo_nome)
                j.set_camisa(nova_camisa)

                print("Jogador atualizado!")
                return

        print("Jogador não encontrado.")

    @staticmethod
    def excluir_jogador():
        print("\n=== EXCLUIR JOGADOR ===")

        id_jogador = int(input("Informe o ID do jogador: "))

        for j in UI.jogadores:
            if j.get_id() == id_jogador:
                UI.jogadores.remove(j)

                print("Jogador removido!")
                return

        print("Jogador não encontrado.")

    @staticmethod
    def listar_jogadores_do_time():
        print("\n=== JOGADORES DO TIME ===")

        id_time = int(input("Informe o ID do time: "))

        encontrou = False

        for j in UI.jogadores:
            if j.get_idTime() == id_time:
                print(j.ToString())
                encontrou = True

        if not encontrou:
            print("Nenhum jogador encontrado nesse time.")

    @staticmethod
    def transferir_jogador():
        print("\n=== TRANSFERIR JOGADOR ===")

        id_jogador = int(input("ID do jogador: "))
        novo_time = int(input("Novo ID do time: "))

        existe = False

        for t in UI.times:
            if t.get_id() == novo_time:
                existe = True
                break

        if not existe:
            print("Time destino não encontrado.")
            return

        for j in UI.jogadores:
            if j.get_id() == id_jogador:
                j.set_idTime(novo_time)

                print("Jogador transferido!")
                return

        print("Jogador não encontrado.")

    @staticmethod
    def menu():
        print("\n========== MENU ==========")
        print("1 - Inserir time")
        print("2 - Listar times")
        print("3 - Atualizar time")
        print("4 - Excluir time")
        print("5 - Inserir jogador")
        print("6 - Listar jogadores")
        print("7 - Editar jogador")
        print("8 - Excluir jogador")
        print("9 - Listar jogadores do time")
        print("10 - Transferir jogador")
        print("0 - Sair")

        return int(input("Escolha uma opção: "))

    @staticmethod
    def main():
        op = 1

        while op != 0:

            op = UI.menu()

            if op == 1:
                UI.inserir_time()

            elif op == 2:
                UI.listar_time()

            elif op == 3:
                UI.atualizar_time()

            elif op == 4:
                UI.excluir_time()

            elif op == 5:
                UI.inserir_jogador()

            elif op == 6:
                UI.listar_jogador()

            elif op == 7:
                UI.editar_jogador()

            elif op == 8:
                UI.excluir_jogador()

            elif op == 9:
                UI.listar_jogadores_do_time()

            elif op == 10:
                UI.transferir_jogador()

            elif op == 0:
                print("Programa encerrado!")

            else:
                print("Opção inválida!")


UI.main()