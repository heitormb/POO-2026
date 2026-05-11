class Time:
    def __init__(self, id, nome, estado):
        self.set_id(id)
        self.set_nome(nome)
        self.set_estado(estado)

    def set_id(self, id):
        if id <= 0:
            raise ValueError("O id deve ser positivo")
        self.id = id

    def set_nome(self, nome):
        if nome == "":
            raise ValueError("O nome não pode ser vazio")
        self.nome = nome

    def set_estado(self, estado):
        if estado == "":
            raise ValueError("O estado não pode ser vazio")
        self.estado = estado

    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    def get_estado(self):
        return self.estado

    def __str__(self):
        return f"{self.id} - {self.nome} - {self.estado}"


class Jogador:
    def __init__(self, id, idTime, nome, camisa):
        self.set_id(id)
        self.set_idTime(idTime)
        self.set_nome(nome)
        self.set_camisa(camisa)

    def set_id(self, id):
        if id <= 0:
            raise ValueError("O id deve ser positivo")
        self.id = id

    def set_idTime(self, idTime):
        if idTime <= 0:
            raise ValueError("O id do time deve ser positivo")
        self.idTime = idTime

    def set_nome(self, nome):
        if nome == "":
            raise ValueError("O nome não pode ser vazio")
        self.nome = nome

    def set_camisa(self, camisa):
        if camisa <= 0:
            raise ValueError("A camisa deve ser positiva")
        self.camisa = camisa

    def get_id(self):
        return self.id

    def get_idTime(self):
        return self.idTime

    def get_nome(self):
        return self.nome

    def get_camisa(self):
        return self.camisa

    def __str__(self):
        return f"{self.id} - {self.idTime} - {self.nome} - {self.camisa}"


class UI:
    Times = []
    Jogadores = []

    @staticmethod
    def main():
        op = 0

        while op != 11:
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
                UI.atualizar_jogador()

            elif op == 8:
                UI.excluir_jogador()

            elif op == 9:
                UI.listar_jogadores_do_time()

            elif op == 10:
                UI.transferir_jogador()

    @staticmethod
    def menu():
        print("\n1-Inserir time")
        print("2-Listar times")
        print("3-Atualizar time")
        print("4-Excluir time")
        print("5-Inserir jogador")
        print("6-Listar jogadores")
        print("7-Atualizar jogador")
        print("8-Excluir jogador")
        print("9-Listar jogadores de um time")
        print("10-Transferir jogador")
        print("11-Fim")

        return int(input("Escolha uma opção: "))

    @classmethod
    def inserir_time(cls):
        id = int(input("Informe o id do time: "))
        nome = input("Informe o nome do time: ")
        estado = input("Informe o estado: ")

        x = Time(id, nome, estado)

        cls.Times.append(x)

        print("Time inserido com sucesso")

    @classmethod
    def listar_time(cls):
        if len(cls.Times) == 0:
            print("Nenhum time cadastrado")

        else:
            for x in cls.Times:
                print(x)

    @classmethod
    def atualizar_time(cls):
        UI.listar_time()

        id = int(input("Informe o id do time: "))

        x = UI.Time_listarID(id)

        if x != None:
            cls.Times.remove(x)

            nome = input("Informe o novo nome: ")
            estado = input("Informe o novo estado: ")

            novo = Time(id, nome, estado)

            cls.Times.append(novo)

            print("Time atualizado")

        else:
            print("Time não encontrado")

    @classmethod
    def excluir_time(cls):
        UI.listar_time()

        id = int(input("Informe o id do time: "))

        x = UI.Time_listarID(id)

        if x != None:
            cls.Times.remove(x)

            print("Time removido")

        else:
            print("Time não encontrado")

    @classmethod
    def inserir_jogador(cls):
        id = int(input("Informe o id do jogador: "))
        idTime = int(input("Informe o id do time: "))
        nome = input("Informe o nome do jogador: ")
        camisa = int(input("Informe a camisa: "))

        if UI.Time_listarID(idTime) == None:
            print("Time não encontrado")
            return

        x = Jogador(id, idTime, nome, camisa)

        cls.Jogadores.append(x)

        print("Jogador inserido com sucesso")

    @classmethod
    def listar_jogador(cls):
        if len(cls.Jogadores) == 0:
            print("Nenhum jogador cadastrado")

        else:
            for x in cls.Jogadores:
                print(x)

    @classmethod
    def atualizar_jogador(cls):
        UI.listar_jogador()

        id = int(input("Informe o id do jogador: "))

        x = UI.Jogador_listarID(id)

        if x != None:
            cls.Jogadores.remove(x)

            idTime = int(input("Informe o novo id do time: "))
            nome = input("Informe o novo nome: ")
            camisa = int(input("Informe a nova camisa: "))

            novo = Jogador(id, idTime, nome, camisa)

            cls.Jogadores.append(novo)

            print("Jogador atualizado")

        else:
            print("Jogador não encontrado")

    @classmethod
    def excluir_jogador(cls):
        UI.listar_jogador()

        id = int(input("Informe o id do jogador: "))

        x = UI.Jogador_listarID(id)

        if x != None:
            cls.Jogadores.remove(x)

            print("Jogador removido")

        else:
            print("Jogador não encontrado")

    @classmethod
    def listar_jogadores_do_time(cls):
        idTime = int(input("Informe o id do time: "))

        encontrou = False

        for x in cls.Jogadores:
            if x.get_idTime() == idTime:
                print(x)
                encontrou = True

        if encontrou == False:
            print("Nenhum jogador encontrado")

    @classmethod
    def transferir_jogador(cls):
        idJogador = int(input("Informe o id do jogador: "))

        jogador = UI.Jogador_listarID(idJogador)

        if jogador == None:
            print("Jogador não encontrado")
            return

        novoTime = int(input("Informe o novo id do time: "))

        if UI.Time_listarID(novoTime) == None:
            print("Time não encontrado")
            return

        jogador.set_idTime(novoTime)

        print("Jogador transferido com sucesso")

    @classmethod
    def Time_listarID(cls, id):
        for x in cls.Times:
            if x.get_id() == id:
                return x

        return None

    @classmethod
    def Jogador_listarID(cls, id):
        for x in cls.Jogadores:
            if x.get_id() == id:
                return x

        return None


UI.main()