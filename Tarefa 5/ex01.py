from datetime import datetime

class Treino:
    def __init__(self, id, n, c, t, nasc):
        self.set_id(id)
        self.set_nome(n)
        self.set_cpf(c)
        self.set_telefone(t)
        self.set_nascimento(nasc)
    def set_id(self, id):
        if id < 0: raise ValueError("Id não pode ser negativo")
        self.__id = id
    def set_nome(self, n):
        if n == "": raise ValueError("Nome não pode ser vazio")
        self.__nome = n
    def set_cpf(self, c):
        if c == "": raise ValueError("CPF não pode ser vazio")
        self.__cpf = c
    def set_telefone(self, t):
        if t == "": raise ValueError("Telefone não pode ser vazio")
        self.__telefone = t
    def set_nascimento(self, nasc):
        if nasc > datetime.now(): raise ValueError("Data não pode estar no futuro")
        self.__nascimento = nasc
    
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_cpf(self): return self.__cpf
    def get_telefone(self): return self.__telefone
    def get_nascimento(self): return self.__nascimento

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__cpf} - {self.__telefone} - {self.__nascimento.strftime("%d/%m/%Y")}"
    def idade(self):
        tempo = datetime.now() - self.__nascimento  # timedelta é contado em dias
        anos = tempo.days // 365
        meses = tempo.days % 365 // 30
        return f"Idade: {anos} ano(s) e {meses} mes(es)"
    
#x = Paciente(1, "Eduardo", "001.002.003-45", "84-90009-1234", datetime(2010, 1, 25))
#print(x)
#print(x.idade())

class PacienteUI:
    __pacientes = []
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = PacienteUI.menu()
            if op == 1: PacienteUI.inserir()
            if op == 2: PacienteUI.listar()
    
    @staticmethod
    def menu():
        print("1-Inserir, 2_Listar, 3-Atualizar, 4-Excluir, 5-Pesquisar, 6-Aniversariantes, 9-Fim")
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
                nasc = datetime.strptime(input("Informe a nova data de nascimento; "), "%d/%m/%Y")
                x.set_nome(nome)
                x.set_cpf(cpf)
                x.set_telefone(fone)
                x.set_nascimento(nasc)

    @classmethod
    def excluir(cls):
        for x in cls.__pacientes: print(x)
        id = int(input("Informe o id do paciente a ser atualizado: "))
        for x in cls.__pacientes:
            if x.get_id() == id:
                cls.pacientes.remove(x)

    @classmethod
    def pesquisar(cls):
        s = input("informe as iniciais do nome: ")
        for x in cls.__pacientes:
            if x.get_nome().startswith(s): print(x)

    @classmethod
    def aniversariantes(cls):
        m = int(input("Informe o mês para a lista de aniversariantes (1 - 12): "))
        for x in cls.__pacientes:
            if x.get_nascimento().month == m: print(x)



PacienteUI.main()