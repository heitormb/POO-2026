import streamlit as st
from service import Service
import time

class PerfilAdminUI:
    @staticmethod
    def main():
        st.header("Alterar Senha")
        op = Service.cliente_listar_id(st.session_state["usuario_id"])
        if op is None:
            st.error("Admin não encontrado.")
            return
        
        st.text_input("E-mail", op.get_email(), disabled=True, key="admin_email")
        senha = st.text_input("Informe a nova senha", op.get_senha(), type="password", key="admin_senha")
        
        if st.button("Atualizar Senha", key="btn_admin_atualizar"):
            Service.cliente_atualizar(op.get_id(), op.get_nome(), op.get_email(), op.get_fone(), op.get_id_convenio(), senha)
            st.success("Senha alterada com sucesso")
            time.sleep(2)
            st.rerun()