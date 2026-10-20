from templates.manterclienteui import ManterClienteUI
from templates.manterservicoui import ManterServicoUI
from templates.manterhorarioui import ManterHorarioUI
from templates.manterprofissionalui import ManterProfissionalUI
from templates.manteratendimentoui import ManterAtendimentoUI
from templates.abrircontaui import AbrirContaUI
from templates.loginui import LoginUI
from templates.perfiladminui import PerfilAdminUI
from templates.perfilclienteui import PerfilClienteUI
from templates.perfilprofissionalui import PerfilProfissionalUI
from templates.agendarservicoui import AgendarServicoUI
from templates.abrirminhaagendaui import AbrirMinhaAgendaUI
from templates.visualizarmeusservicosui import VisualizarMeusServicosUI
from templates.visualizarminhaagendaui import VisualizarMinhaAgendaUI
from templates.confirmarservicoui import ConfirmarServicoUI
from service import Service
import streamlit as st

class IndexUI:

    @staticmethod
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"], key="menu_visitante")
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()

    @staticmethod
    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Agendar Serviço", "Meus Serviços"], key="menu_cliente")
        if op == "Meus Dados": PerfilClienteUI.main()
        if op == "Agendar Serviço": AgendarServicoUI.main()
        if op == "Meus Serviços": VisualizarMeusServicosUI.main()

    @staticmethod
    def menu_profissional():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Abrir Minha Agenda", "Minha Agenda", "Confirmar Serviço"], key="menu_profissional")
        if op == "Meus Dados": PerfilProfissionalUI.main()
        if op == "Abrir Minha Agenda": AbrirMinhaAgendaUI.main()
        if op == "Minha Agenda": VisualizarMinhaAgendaUI.main()
        if op == "Confirmar Serviço": ConfirmarServicoUI.main()

    @staticmethod
    def menu_admin():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Clientes", "Serviços", "Horários", "Profissionais", "Atendimentos"], key="menu_admin")
        if op == "Meus Dados": PerfilAdminUI.main()
        if op == "Clientes": ManterClienteUI.main()
        if op == "Serviços": ManterServicoUI.main()
        if op == "Horários": ManterHorarioUI.main()
        if op == "Profissionais": ManterProfissionalUI.main()
        if op == "Atendimentos": ManterAtendimentoUI.main()

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
                # Certifique-se de que no seu LoginUI você também armazena st.session_state["usuario_tipo"]
                tipo = st.session_state.get("usuario_tipo", "cliente")
                if tipo == "cliente": 
                    IndexUI.menu_cliente()
                else: 
                    IndexUI.menu_profissional()
            IndexUI.sair_do_sistema()

    @staticmethod
    def main():
        Service.cliente_criar_admin()
        IndexUI.sidebar()

IndexUI.main()