class Profissional:
    def __init__(self, id, nome, email, especialidade, senha):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_especialidade(especialidade)
        self.set_senha(senha)

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def get_especialidade(self):
        return self.__especialidade

    def get_senha(self):
        return self.__senha

    def set_id(self, id):
        self.__id = id

    def set_nome(self, nome):
        if not nome or nome.strip() == "":
            raise ValueError("O nome do profissional não pode ser vazio.")
        self.__nome = nome

    def set_email(self, email):
        if not email or email.strip() == "":
            raise ValueError("O e-mail do profissional não pode ser vazio.")
        self.__email = email

    def set_especialidade(self, especialidade):
        self.__especialidade = especialidade

    def set_senha(self, senha):
        if not senha or senha.strip() == "":
            raise ValueError("A senha do profissional não pode ser vazia.")
        self.__senha = senha

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__especialidade}"

    def to_json(self):
        return {
            "id": self.__id,
            "nome": self.__nome,
            "email": self.__email,
            "especialidade": self.__especialidade,
            "senha": self.__senha
        }

    @staticmethod
    def from_json(dic):
        return Profissional(
            dic["id"],
            dic["nome"],
            dic["email"],
            dic["especialidade"],
            dic.get("senha", "1234")
        )