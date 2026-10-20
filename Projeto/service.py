from datetime import datetime
from models.cliente import Cliente
from models.clientedao import ClienteDAO
from models.servico import Servico
from models.servicodao import ServicoDAO
from models.horario import Horario
from models.horariodao import HorarioDAO
from models.profissional import Profissional
from models.profissionaldao import ProfissionalDAO
from models.atendimento import Atendimento
from models.atendimentodao import AtendimentoDAO
from models.convenio import Convenio
from models.conveniodao import ConvenioDAO

class Service:
    @staticmethod
    def cliente_inserir(nome, email, fone, id_convenio, senha):
        obj = Cliente(0, nome, email, fone, id_convenio, senha)
        ClienteDAO().inserir(obj)
    
    @staticmethod
    def cliente_listar():
        r = ClienteDAO().listar()
        r.sort(key = lambda obj : obj.get_nome().casefold())
        return r
        
    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO().listar_id(id)
        
    @staticmethod
    def cliente_atualizar(id, nome, email, fone, id_convenio, senha):
        obj = Cliente(id, nome, email, fone, id_convenio, senha)
        ClienteDAO().atualizar(obj)
        
    @staticmethod
    def cliente_excluir(id):
        ClienteDAO().excluir(id)
        
    @staticmethod
    def cliente_criar_admin():
        for c in Service.cliente_listar():
            if c.get_email() == "admin": return
        Service.cliente_inserir("admin", "admin", "fone", 1, "admin")
        
    @staticmethod
    def cliente_autenticar(email, senha):
        for c in Service.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id": c.get_id(), "nome": c.get_nome()}
        return None

    @staticmethod
    def profissional_inserir(nome, email, especialidade, senha):
        obj = Profissional(0, nome, email, especialidade, senha)
        ProfissionalDAO().inserir(obj)
        
    @staticmethod
    def profissional_listar():
        r = ProfissionalDAO().listar()
        r.sort(key = lambda obj : obj.get_nome().casefold())
        return r
        
    @staticmethod
    def profissional_listar_id(id):
        return ProfissionalDAO().listar_id(id)
        
    @staticmethod
    def profissional_atualizar(id, nome, email, especialidade, senha):
        obj = Profissional(id, nome, email, especialidade, senha)
        ProfissionalDAO().atualizar(obj)
        
    @staticmethod
    def profissional_excluir(id):
        ProfissionalDAO().excluir(id)

    @staticmethod
    def profissional_autenticar(email, senha):
        for p in Service.profissional_listar():
            if p.get_email() == email and p.get_senha() == senha:
                return {"id": p.get_id(), "nome": p.get_nome()}
        return None

    @staticmethod
    def servico_inserir(descricao, valor):
        obj = Servico(0, descricao, valor)
        ServicoDAO().inserir(obj)
        
    @staticmethod
    def servico_listar():
        r = ServicoDAO().listar()
        r.sort(key = lambda obj : obj.get_descricao().casefold())
        return r
        
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
    def horario_inserir(data, confirmado, id_cliente, id_servico, id_profissional):
        c = Horario(0, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_profissional(id_profissional)
        HorarioDAO().inserir(c)
        
    @staticmethod
    def horario_listar():
        r = HorarioDAO().listar()
        r.sort(key = lambda obj : obj.get_data())
        return r
        
    @staticmethod
    def horario_listar_id(id):
        return HorarioDAO().listar_id(id) 
        
    @staticmethod
    def horario_listar_disponiveis(id_profissional):
        r = []
        agora = datetime.now()
        for h in Service.horario_listar():
            if h.get_data() >= agora and h.get_confirmado() == False and (h.get_id_cliente() is None or h.get_id_cliente() == 0) and h.get_id_profissional() == id_profissional:
                r.append(h)
        r.sort(key = lambda h : h.get_data())
        return r

    @staticmethod
    def horario_atualizar(id, data, confirmado, id_cliente, id_servico, id_profissional):
        c = Horario(id, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_profissional(id_profissional)
        HorarioDAO().atualizar(c)
        
    @staticmethod
    def horario_excluir(id):
        HorarioDAO().excluir(id)

    @staticmethod
    def atendimento_inserir(data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario):
      a = Atendimento(0, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario)
      AtendimentoDAO().inserir(a)
      
    @staticmethod
    def atendimento_listar():
      return AtendimentoDAO().listar()
      
    @staticmethod
    def atendimento_listar_id(id):
      return AtendimentoDAO().listar_id(id)
      
    @staticmethod
    def atendimento_atualizar(id, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario):
      a = Atendimento(id, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario)
      AtendimentoDAO().atualizar(a)
      
    @staticmethod
    def atendimento_excluir(id):
      a = AtendimentoDAO().listar_id(id)
      if a is not None:
        AtendimentoDAO().excluir(a)

    @staticmethod
    def convenio_inserir(nome, contato, fone):
        obj = Convenio(0, nome, contato, fone)
        ConvenioDAO().inserir(obj)
        
    @staticmethod
    def convenio_listar():
        return ConvenioDAO().listar()
        
    @staticmethod
    def convenio_listar_id(id):
        return ConvenioDAO().listar_id(id)
        
    @staticmethod
    def convenio_atualizar(id, nome, contato, fone):
        obj = Convenio(id, nome, contato, fone)
        ConvenioDAO().atualizar(obj)
        
    @staticmethod
    def convenio_excluir(id):
        ConvenioDAO().excluir(id)