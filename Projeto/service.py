from models.cliente import Cliente
from models.clientedao import ClienteDAO
from models.atendimento import Atendimento
from models.atendimentodao import AtendimentoDAO

class Service:
    # --- CLIENTE ---
    @staticmethod
    def cliente_inserir(id, nome, email, fone):
        obj = Cliente(id, nome, email, fone)
        ClienteDAO().inserir(obj)

    @staticmethod
    def cliente_listar():
        return ClienteDAO().listar()

    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO().listar_id(id)

    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        obj = Cliente(id, nome, email, fone)
        ClienteDAO().atualizar(obj)

    @staticmethod
    def cliente_excluir(id):
        ClienteDAO().excluir(id)

    # --- ATENDIMENTO ---
    @staticmethod
    def atendimento_inserir(id, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario):
        obj = Atendimento(id, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario)
        AtendimentoDAO().inserir(obj)

    @staticmethod
    def atendimento_listar():
        return AtendimentoDAO().listar()

    @staticmethod
    def atendimento_listar_id(id):
        return AtendimentoDAO().listar_id(id)

    @staticmethod
    def atendimento_atualizar(id, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario):
        obj = Atendimento(id, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario)
        AtendimentoDAO().atualizar(obj)

    @staticmethod
    def atendimento_excluir(id):
        obj = AtendimentoDAO().listar_id(id)
        if obj:
            AtendimentoDAO().excluir(obj)