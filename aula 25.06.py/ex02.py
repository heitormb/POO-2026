import json
from pathlib import Path
from enum import Enum

class Grupo(Enum):
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6
    G = 7
    H = 8
    I = 9
    J = 10
    K = 11
    L = 12

class Fase(Enum):
    Grupos = 1
    DezesseiasAvos = 2
    Oitavas = 3
    Quartas = 4
    Semifinais = 5
    TerceiroLugar = 6
    Final = 7


class Pais:
    def __init__(self, i, n, s, g):
        self.set_id(i)
        self.set_nome(n)
        self.set_sigla(s)
        self.set_grupo(g)

    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome deve ser informado")
        self.__nome = nome
    def set_sigla(self, sigla):
        if sigla == "": raise ValueError("Sigla deve ser informada")
        self.__sigla = sigla
    def set_grupo(self, grupo):
        self.__grupo = grupo

    def get_id(self) : return self.__id
    def get_nome(self) : return self.__nome
    def get_sigla(self) : return self.__sigla
    def get_grupo(self) : return self.__grupo

    def __str__(self):
        return f"{self.__id} - {self.__nome} ({self.__sigla}) - Grupo {self.__grupo.name}"

    def to_json(self):
        return { "id": self.__id, "nome": self.__nome, "sigla": self.__sigla, "grupo": self.__grupo.name }

    @staticmethod
    def from_json(dic):
        return Pais(dic["id"], dic["nome"], dic["sigla"], Grupo[dic["grupo"]])


class Jogo:
    def __init__(self, i, ip1, ip2, g1, g2, f, dh):
        self.set_id(i)
        self.set_id_pais1(ip1)
        self.set_id_pais2(ip2)
        self.set_gols1(g1)
        self.set_gols2(g2)
        self.set_fase(f)
        self.set_data_hora(dh)

    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id
    def set_id_pais1(self, id_pais1):
        if id_pais1 < 0: raise ValueError("Id do país 1 deve ser positivo")
        self.__id_pais1 = id_pais1
    def set_id_pais2(self, id_pais2):
        if id_pais2 < 0: raise ValueError("Id do país 2 deve ser positivo")
        self.__id_pais2 = id_pais2
    def set_gols1(self, gols1):
        if gols1 < 0: raise ValueError("Gols devem ser positivos")
        self.__gols1 = gols1
    def set_gols2(self, gols2):
        if gols2 < 0: raise ValueError("Gols devem ser positivos")
        self.__gols2 = gols2
    def set_fase(self, fase):
        self.__fase = fase
    def set_data_hora(self, data_hora):
        if data_hora == "": raise ValueError("Data e hora devem ser informadas")
        self.__data_hora = data_hora

    def get_id(self) : return self.__id
    def get_id_pais1(self) : return self.__id_pais1
    def get_id_pais2(self) : return self.__id_pais2
    def get_gols1(self) : return self.__gols1
    def get_gols2(self) : return self.__gols2
    def get_fase(self) : return self.__fase
    def get_data_hora(self) : return self.__data_hora

    def __str__(self):
        return f"{self.__id} - País {self.__id_pais1} {self.__gols1} x {self.__gols2} País {self.__id_pais2} - {self.__fase.name} - {self.__data_hora}"

    def to_json(self):
        return { "id": self.__id, "id_pais1": self.__id_pais1, "id_pais2": self.__id_pais2, "gols1": self.__gols1, "gols2": self.__gols2, "fase": self.__fase.name, "data_hora": self.__data_hora }

    @staticmethod
    def from_json(dic):
        return Jogo(dic["id"], dic["id_pais1"], dic["id_pais2"], dic["gols1"], dic["gols2"], Fase[dic["fase"]], dic["data_hora"])


class UI:
    __paises = []
    __jogos = []
    __paises_json = Path(__file__).resolve().parent / "paises.json"
    __jogos_json = Path(__file__).resolve().parent / "jogos.json"

    @staticmethod
    def main():
        UI.abrir()
        op = 0
        while op != 7:
            op = UI.menu()
            if op == 1: UI.inserir_pais()
            if op == 2: UI.listar_paises()
            if op == 3: UI.inserir_jogo()
            if op == 4: UI.listar_jogos()
            if op == 5: UI.salvar()
            if op == 6: UI.abrir()

    @staticmethod
    def menu():
        print("\n===== COPA DO MUNDO 2026 =====")
        print("1 - Inserir país")
        print("2 - Listar países")
        print("3 - Inserir jogo")
        print("4 - Listar jogos")
        print("5 - Salvar")
        print("6 - Abrir")
        print("7 - Sair")
        return int(input("Opção: "))

    @staticmethod
    def inserir_pais():
        try:
            i = int(input("ID: "))
            n = input("Nome: ")
            s = input("Sigla: ")
            print("Grupos:", ", ".join(g.name for g in Grupo))
            g = Grupo[input("Grupo: ").upper()]
            p = Pais(i, n, s, g)
            UI.__paises.append(p)
            print("País inserido com sucesso!")
        except (ValueError, KeyError) as ve:
            print(f"Erro: {ve}")

    @staticmethod
    def listar_paises():
        if len(UI.__paises) == 0:
            print("Nenhum país cadastrado.")
            return
        for p in UI.__paises:
            print(p)

    @staticmethod
    def inserir_jogo():
        try:
            i = int(input("ID: "))
            ip1 = int(input("ID do país 1: "))
            ip2 = int(input("ID do país 2: "))
            g1 = int(input("Gols do país 1: "))
            g2 = int(input("Gols do país 2: "))
            print("Fases:", ", ".join(f.name for f in Fase))
            f = Fase[input("Fase: ")]
            dh = input("Data e hora (DD/MM/AAAA HH:MM): ")
            j = Jogo(i, ip1, ip2, g1, g2, f, dh)
            UI.__jogos.append(j)
            print("Jogo inserido com sucesso!")
        except (ValueError, KeyError) as ve:
            print(f"Erro: {ve}")

    @staticmethod
    def listar_jogos():
        if len(UI.__jogos) == 0:
            print("Nenhum jogo cadastrado.")
            return
        for j in UI.__jogos:
            print(j)

    @staticmethod
    def salvar():
        with open(UI.__paises_json, "w") as f:
            json.dump([p.to_json() for p in UI.__paises], f, indent=4)
        with open(UI.__jogos_json, "w") as f:
            json.dump([j.to_json() for j in UI.__jogos], f, indent=4)
        print("Dados salvos com sucesso!")

    @staticmethod
    def abrir():
        if UI.__paises_json.exists():
            with open(UI.__paises_json, "r") as f:
                lista = json.load(f)
                UI.__paises = [Pais.from_json(p) for p in lista]
        if UI.__jogos_json.exists():
            with open(UI.__jogos_json, "r") as f:
                lista = json.load(f)
                UI.__jogos = [Jogo.from_json(j) for j in lista]


UI.main()