import json
from pathlib import Path
from datetime import datetime

class Contato:
    def __init__(self, i, n, e, f, d):
        self.set_id(i)
        self.set_nome(n)
        self.set_email(e)
        self.set_fone(f)
        self.set_nascimento(d)

    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome deve ser informado")
        self.__nome = nome
    def set_email(self, email):
        if email == "": raise ValueError("E-mail deve ser informado")
        self.__email = email
    def set_fone(self, fone):
        if fone == "": raise ValueError("Fone deve ser informado")
        self.__fone = fone
    def set_nascimento(self, nascimento):
        if nascimento == "": raise ValueError("Data de nascimento deve ser informada")
        self.__nascimento = nascimento

    def get_id(self) : return self.__id
    def get_nome(self) : return self.__nome
    def get_email(self) : return self.__email
    def get_fone(self) : return self.__fone
    def get_nascimento(self) : return self.__nascimento

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone} - {self.__nascimento}"

    def to_json(self):
        return { "id": self.__id, "nome": self.__nome, "email": self.__email, "fone": self.__fone, "nascimento": self.__nascimento }

    @staticmethod
    def from_json(dic):
        return Contato(dic["id"], dic["nome"], dic["email"], dic["fone"], dic["nascimento"])


class ContatoUI:
    __objetos = []
    __contatos_json = Path(__file__).resolve().parent / "contatos.json"

    @staticmethod
    def main():
        ContatoUI.abrir()
        op = 0
        while op != 9:
            op = ContatoUI.menu()
            if op == 1: ContatoUI.inserir()
            if op == 2: ContatoUI.listar()
            if op == 3: ContatoUI.listar_id()
            if op == 4: ContatoUI.atualizar()
            if op == 5: ContatoUI.excluir()
            if op == 6: ContatoUI.pesquisar()
            if op == 7: ContatoUI.aniversariantes()
            if op == 8: ContatoUI.salvar()

    @staticmethod
    def menu():
        print("\n===== AGENDA DE CONTATOS =====")
        print("1 - Inserir contato")
        print("2 - Listar todos")
        print("3 - Listar por ID")
        print("4 - Atualizar contato")
        print("5 - Excluir contato")
        print("6 - Pesquisar por iniciais")
        print("7 - Aniversariantes do mês")
        print("8 - Salvar")
        print("9 - Sair")
        return int(input("Opção: "))

    @staticmethod
    def inserir():
        try:
            i = int(input("ID: "))
            n = input("Nome: ")
            e = input("E-mail: ")
            f = input("Fone: ")
            d = input("Nascimento (DD/MM/AAAA): ")
            c = Contato(i, n, e, f, d)
            ContatoUI.__objetos.append(c)
            print("Contato inserido com sucesso!")
        except ValueError as ve:
            print(f"Erro: {ve}")

    @staticmethod
    def listar():
        if len(ContatoUI.__objetos) == 0:
            print("Nenhum contato cadastrado.")
            return
        for c in ContatoUI.__objetos:
            print(c)

    @staticmethod
    def listar_id():
        id = int(input("ID: "))
        for c in ContatoUI.__objetos:
            if c.get_id() == id:
                print(c)
                return
        print("Contato não encontrado.")

    @staticmethod
    def atualizar():
        id = int(input("ID do contato a atualizar: "))
        for c in ContatoUI.__objetos:
            if c.get_id() == id:
                try:
                    n = input(f"Nome [{c.get_nome()}]: ") or c.get_nome()
                    e = input(f"E-mail [{c.get_email()}]: ") or c.get_email()
                    f = input(f"Fone [{c.get_fone()}]: ") or c.get_fone()
                    d = input(f"Nascimento [{c.get_nascimento()}]: ") or c.get_nascimento()
                    c.set_nome(n)
                    c.set_email(e)
                    c.set_fone(f)
                    c.set_nascimento(d)
                    print("Contato atualizado com sucesso!")
                except ValueError as ve:
                    print(f"Erro: {ve}")
                return
        print("Contato não encontrado.")

    @staticmethod
    def excluir():
        id = int(input("ID do contato a excluir: "))
        for c in ContatoUI.__objetos:
            if c.get_id() == id:
                ContatoUI.__objetos.remove(c)
                print("Contato excluído com sucesso!")
                return
        print("Contato não encontrado.")

    @staticmethod
    def pesquisar():
        iniciais = input("Iniciais do nome: ").lower()
        encontrados = [c for c in ContatoUI.__objetos if c.get_nome().lower().startswith(iniciais)]
        if len(encontrados) == 0:
            print("Nenhum contato encontrado.")
            return
        for c in encontrados:
            print(c)

    @staticmethod
    def aniversariantes():
        mes = int(input("Mês (1-12): "))
        encontrados = []
        for c in ContatoUI.__objetos:
            try:
                data = datetime.strptime(c.get_nascimento(), "%d/%m/%Y")
                if data.month == mes:
                    encontrados.append(c)
            except:
                pass
        if len(encontrados) == 0:
            print("Nenhum aniversariante neste mês.")
            return
        for c in encontrados:
            print(c)

    @staticmethod
    def abrir():
        if ContatoUI.__contatos_json.exists():
            with open(ContatoUI.__contatos_json, "r") as f:
                lista = json.load(f)
                ContatoUI.__objetos = [Contato.from_json(c) for c in lista]

    @staticmethod
    def salvar():
        with open(ContatoUI.__contatos_json, "w") as f:
            json.dump([c.to_json() for c in ContatoUI.__objetos], f, indent=4)
        print("Contatos salvos com sucesso!")


ContatoUI.main()