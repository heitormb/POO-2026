import streamlit as st
from service import Service
import time

class PerfilProfissionalUI:
    @staticmethod
    def main():
        st.header("Meus Dados (Profissional)")
        op = Service.profissional_listar_id(st.session_state["usuario_id"])
        if op is None:
            st.error("Profissional não encontrado.")
            return
        
        nome = st.text_input("Informe o novo nome", op.get_nome(), key="perfil_prof_nome")
        email = st.text_input("Informe o novo e-mail", op.get_email(), key="perfil_prof_email")
        especialidade = st.text_input("Informe a nova especialidade", op.get_especialidade(), key="perfil_prof_esp")
        senha = st.text_input("Informe a nova senha", op.get_senha(), type="password", key="perfil_prof_senha")
        
        if st.button("Atualizar", key="btn_perfil_prof_atualizar"):
            id = op.get_id()
            Service.profissional_atualizar(id, nome, email, especialidade, senha)
            st.success("Dados atualizados com sucesso")
            time.sleep(2)
            st.rerun()