from datetime import datetime

class Paciente:
    def __init__(self, nome, cpf, fone, nascimento):
        self.__nome = nome
        self.__cpf = cpf
        self.__fone = fone
        self.__nascimento = nascimento
    def __str__(self):
        return f"{self.__nome} - {self.__cpf} - {self.__fone} - {self.__nascimento.strftime('%d/%m/%Y')}"
    def idade(self):
        x = datetime.now() - self.__nascimento   # idade
        dias = x.days                            # dias vividos
        anos = dias // 365
        meses = dias % 365 // 30
        return f"{anos} ano(s) e {meses} mes(es)"
    
x = Paciente("Nome", "123", "456", datetime(2009, 7, 28))
print(x)
print(x.idade())