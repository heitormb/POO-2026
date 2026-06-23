import json

class Cliente:
    def __init__(self, id, nome, email, fone):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
   
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

    def get_id(self) : return self.__id
    def get_nome(self) : return self.__nome
    def get_email(self) : return self.__email
    def get_fone(self) : return self.__fone

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"
   
    def to_json(self):
        return { "id":self.__id, "nome":self.__nome, "email":self.__email, "fone":self.__fone }
   
    @staticmethod
    def from_json(dic):
        return Cliente(dic["id"], dic["nome"], dic["email"], dic["fone"])

class PacienteUI:
    __pacientes = []
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = PacienteUI.menu()
            if op == 1: PacienteUI.inserir()
            if op == 2: PacienteUI.listar()
            if op == 3: PacienteUI.atualizar()
            if op == 4: PacienteUI.excluir()

    @staticmethod
    def menu():
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 5-Pesquisar, 6-Aniversariantes, 9-Fim")
        return int(input("Informe uma opção: "))

    @classmethod
    def inserir(cls):
        id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        cpf = input("Informe o CPF: ")
        fone = input("Informe o telefone: ")
        nasc = datetime.strptime(input("Informe a data de nascimento: "), "%d/%m/%Y")
        x = Paciente(id, nome, cpf, fone, nasc)
        cls.__pacientes.append(x)

    @classmethod
    def listar(cls):                
        for x in cls.__pacientes: print(x, x.idade())

    @classmethod
    def atualizar(cls):
        for x in cls.__pacientes: print(x)
        id = int(input("Informe o id do paciente a ser atualizado: "))
        for x in cls.__pacientes:
            if x.get_id() == id:
                nome = input("Informe o novo nome: ")
                cpf = input("Informe o novo CPF: ")
                fone = input("Informe o novo telefone: ")
                nasc = datetime.strptime(input("Informe a nova data de nascimento: "), "%d/%m/%Y")
                x.set_nome(nome)
                x.set_cpf(cpf)
                x.set_telefone(fone)
                x.set_nascimento(nasc)

    @classmethod
    def excluir(cls):
        for x in cls.__pacientes: print(x)
        id = int(input("Informe o id do paciente a ser excluído: "))
        for x in cls.__pacientes:
            if x.get_id() == id:
                cls.__pacientes.remove(x)

PacienteUI.main()