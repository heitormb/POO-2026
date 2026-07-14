from models.cliente import Cliente
from models.clientedao import ClienteDAO
from models.servico import Servico
from models.servicodao import ServicoDAO
from models.profissional import Profissional
from models.profissionaldao import ProfissionalDAO

class Service:
    @staticmethod
    def cliente_inserir(id, nome, email, fone, senha):
        obj = Cliente(id, nome, email, fone, senha)
        ClienteDAO().inserir(obj)

    @staticmethod
    def cliente_listar():
        return ClienteDAO().listar()

    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO().listar_id(id)

    @staticmethod
    def cliente_atualizar(id, nome, email, fone, senha):
        obj = Cliente(id, nome, email, fone, senha)
        ClienteDAO().atualizar(obj)

    @staticmethod
    def cliente_excluir(id):
        ClienteDAO().excluir(id)

    @staticmethod
    def servico_inserir(id, descricao, valor):
        obj = Servico(id, descricao, valor)
        ServicoDAO().inserir(obj)

    @staticmethod
    def servico_listar():
        return ServicoDAO().listar()

    @staticmethod
    def servico_listar_id(id):
        return ServicoDAO().listar_id(id)

    @staticmethod
    def servico_atualizar(id, descricao, valor):
        obj = Servico(id, descricao, valor)
        ServicoDAO().atualizar(obj)

    @staticmethod
    def servico_excluir(id):
        ServicoDAO().excluir(id)

    @staticmethod
    def profissional_inserir(id, nome, email, senha, especialidade):
        obj = Profissional(id, nome, email, senha, especialidade)
        ProfissionalDAO().inserir(obj)

    @staticmethod
    def profissional_listar():
        return ProfissionalDAO().listar()

    @staticmethod
    def profesional_listar_id(id):
        return ProfissionalDAO().listar_id(id)

    @staticmethod
    def profissional_pesquisar_nome(nome):
        resultado = []
        for obj in ProfissionalDAO().listar():
            if nome.lower() in obj.get_nome().lower():
                resultado.append(obj)
        return resultado

    @staticmethod
    def profissional_atualizar(id, nome, email, senha, especialidade):
        obj = Profissional(id, nome, email, senha, especialidade)
        ProfissionalDAO().atualizar(obj)

    @staticmethod
    def profissional_excluir(id):
        ProfissionalDAO().excluir(id)