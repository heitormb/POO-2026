import streamlit as st
from service import Service
import time

class PerfilClienteUI:
    @staticmethod
    def main():
        st.header("Meus Dados")
        op = Service.cliente_listar_id(st.session_state["usuario_id"])
        nome = st.text_input("Informe o novo nome", op.get_nome(), key="perfil_nome")
        email = st.text_input("Informe o novo e-mail", op.get_email(), key="perfil_email")
        fone = st.text_input("Informe o novo fone", op.get_fone(), key="perfil_fone")
        senha = st.text_input("Informe a nova senha", op.get_senha(), type="password", key="perfil_senha")
        if st.button("Atualizar", key="btn_perfil_atualizar"):
            id = op.get_id()
            Service.cliente_atualizar(id, nome, email, fone, op.get_id_convenio(), senha)
            st.success("Cliente atualizado com sucesso")
            time.sleep(2)
            st.rerun()