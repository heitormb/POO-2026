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
from templates.agendarservicoui import AgendarServicoUI
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
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Agendar Serviço"], key="menu_cliente")
        if op == "Meus Dados": 
            PerfilClienteUI.main()
        elif op == "Agendar Serviço": 
            AgendarServicoUI.main()

    @staticmethod
    def menu_profissional():
        op = st.sidebar.selectbox("Menu", ["Meus Dados"], key="menu_profissional")
        if op == "Meus Dados": 
            PerfilProfissionalUI.main()

    @staticmethod
    def menu_admin():
        op = st.sidebar.selectbox(
            "Menu", 
            ["Clientes", "Serviços", "Horários", "Profissionais", "Atendimentos", "Convênios"], 
            key="menu_admin"
        )
        if op == "Clientes": 
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