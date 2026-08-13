from datetime import datetime

class Paciente:
    def __init__(self, nome, cpf, telefone, nascimento):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__nascimento = nascimento

    def __str__(self):
        return f"Nome = {self.__nome}, CPF = {self.__cpf}, Telefone = {self.__telefone}, Nascimento = {self.__nascimento.strftime('%d/%m/%Y')}"

    def idade(self):
        x = datetime.now() - self.__nascimento
        dias = x.days
        anos = dias // 365
        meses = dias % 365 // 30
        return f"{anos} ano(s) e {meses} mes(es)"

if __name__ == "__main__":
    x = Paciente("Nome", "123", "456", datetime(2010, 12, 20))
    print(x)
    print(x.idade())