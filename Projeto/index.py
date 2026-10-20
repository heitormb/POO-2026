from templates.manterclienteui import ManterClienteUI
from templates.manterservicoui import ManterServicoUI
from templates.manterhorarioui import ManterHorarioUI
from templates.manterprofissionalui import ManterProfissionalUI
from templates.manteratendimentoui import ManterAtendimentoUI
from templates.manterconvenioui import ManterConvenioUI
from templates.abrircontaui import AbrirContaUI
from templates.loginui import LoginUI
from templates.perfilclienteui import PerfilClienteUI
from service import Service
import streamlit as st

class IndexUI:
    def main():
        Service.cliente_criar_admin()
        IndexUI.sidebar()
        op = st.sidebar.selectbox("Menu", ["Clientes", "Serviços", "Horários", "Profissionais", "Atendimentos", "Convênios"])
        if op == "Clientes": ManterClienteUI.main()
        if op == "Serviços": ManterServicoUI.main()
        if op == "Horários": ManterHorarioUI.main()
        if op == "Profissionais": ManterProfissionalUI.main()
        if op == "Atendimentos": ManterAtendimentoUI.main()
        if op == "Convênios": ManterConvenioUI.main()

        def menu_visitante():
            op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
            if op == "Entrar no Sistema": LoginUI.main()
            if op == "Abrir Conta": AbrirContaUI.main()

        def menu_cliente():
            op = st.sidebar.selectbox("Menu", ["Meus Dados"])
            if op == "Meus Dados": PerfilClienteUI.main()

        def menu_admin():
            op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Serviços", "Cadastro de Horários", "Cadastro de Profissionais"])
            if op == "Cadastro de Clientes": ManterClienteUI.main()
            if op == "Cadastro de Serviços": ManterServicoUI.main()
            if op == "Cadastro de Horários": ManterHorarioUI.main()
            if op == "Cadastro de Profissionais": ManterProfissionalUI.main()

        def sair_do_sistema():
            if st.sidebar.button("Sair"):
                del st.session_state["usuario_id"]
                del st.session_state["usuario_nome"]
                st.rerun()

        def sidebar():
            if "usuario_id" not in st.session_state:
                IndexUI.menu_visitante()
            else:
                admin = st.session_state["usuario_nome"] == "admin"
                st.sidebar.write("Bem-vindo(a), " + st.session_state["usuario_nome"])
                if admin: IndexUI.menu_admin()
                else: IndexUI.menu_cliente()
                IndexUI.sair_do_sistema()

IndexUI.main()