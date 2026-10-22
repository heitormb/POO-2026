from templates.manterclienteui import ManterClienteUI
from templates.manterservicoui import ManterServicoUI
from templates.manterhorarioui import ManterHorarioUI
from templates.manterprofissionalui import ManterProfissionalUI
from templates.manteratendimentoui import ManterAtendimentoUI
from templates.manterconvenioui import ManterConvenioUI
from templates.abrircontaui import AbrirContaUI
from templates.loginui import LoginUI
from templates.perfilclienteui import PerfilClienteUI
from templates.perfilprofissionalui import PerfilProfissionalUI
from templates.perfiladminui import PerfilAdminUI
from templates.agendarservicoui import AgendarServicoUI
from templates.abrirminhaagendaui import AbrirMinhaAgendaUI
from templates.visualizarminhaagendaui import VisualizarMinhaAgendaUI
from templates.visualizarmeusservicosui import VisualizarMeusServicosUI
from templates.confirmarservicoui import ConfirmarServicoUI
from templates.registraratendimentoui import RegistrarAtendimentoUI
from templates.pagaratendimentoui import PagarAtendimentoUI
from templates.totalizaratendimentosui import TotalizarAtendimentosUI
from templates.listarhorariosconfirmadoshojeui import ListarHorariosConfirmadosHojeUI
from templates.listaragendaprofissionalui import ListarAgendaProfissionalUI
from service import Service
import streamlit as st

class IndexUI:

    @staticmethod
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"], key="menu_visitante")
        if op == "Entrar no Sistema": 
            LoginUI.main()
        elif op == "Abrir Conta": 
            AbrirContaUI.main()

    @staticmethod
    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Agendar Serviço", "Meus Serviços", "Pagar Atendimento"], key="menu_cliente")
        if op == "Meus Dados": 
            PerfilClienteUI.main()
        elif op == "Agendar Serviço": 
            AgendarServicoUI.main()
        elif op == "Meus Serviços": 
            VisualizarMeusServicosUI.main()
        elif op == "Pagar Atendimento":
            PagarAtendimentoUI.main()

    @staticmethod
    def menu_profissional():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Abrir Minha Agenda", "Minha Agenda", "Confirmar Serviço", "Registrar Atendimento"], key="menu_profissional")
        if op == "Meus Dados": 
            PerfilProfissionalUI.main()
        elif op == "Abrir Minha Agenda":
            AbrirMinhaAgendaUI.main()
        elif op == "Minha Agenda":
            VisualizarMinhaAgendaUI.main()
        elif op == "Confirmar Serviço":
            ConfirmarServicoUI.main()
        elif op == "Registrar Atendimento":
            RegistrarAtendimentoUI.main()

    @staticmethod
    def menu_admin():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Clientes", "Serviços", "Horários", "Profissionais", "Atendimentos", "Convênios", "Totalizar Atendimentos", "Horários Confirmados Hoje", "Agenda do Profissional"], key="menu_admin")
        if op == "Meus Dados":
            PerfilAdminUI.main()
        elif op == "Clientes": 
            ManterClienteUI.main()
        elif op == "Serviços": 
            ManterServicoUI.main()
        elif op == "Horários": 
            ManterHorarioUI.main()
        elif op == "Profissionais": 
            ManterProfissionalUI.main()
        elif op == "Atendimentos": 
            ManterAtendimentoUI.main()
        elif op == "Convênios": 
            ManterConvenioUI.main()
        elif op == "Totalizar Atendimentos":
            TotalizarAtendimentosUI.main()
        elif op == "Horários Confirmados Hoje":
            ListarHorariosConfirmadosHojeUI.main()
        elif op == "Agenda do Profissional":
            ListarAgendaProfissionalUI.main()

    @staticmethod
    def sair_do_sistema():
        if st.sidebar.button("Sair", key="btn_sair_sistema"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            if "usuario_tipo" in st.session_state:
                del st.session_state["usuario_tipo"]
            st.rerun()

    @staticmethod
    def sidebar():
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            admin = st.session_state["usuario_nome"] == "admin"
            st.sidebar.write("Bem-vindo(a), " + st.session_state["usuario_nome"])
            if admin: 
                IndexUI.menu_admin()
            else: 
                tipo = st.session_state.get("usuario_tipo", "cliente")
                if tipo == "profissional":
                    IndexUI.menu_profissional()
                else:
                    IndexUI.menu_cliente()
            IndexUI.sair_do_sistema()

    @staticmethod
    def main():
        Service.cliente_criar_admin()
        IndexUI.sidebar()

IndexUI.main()