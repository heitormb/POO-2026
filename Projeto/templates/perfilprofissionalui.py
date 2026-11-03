import streamlit as st
from service import Service
import time

class PerfilProfissionalUI:
    @staticmethod
    def main():
        st.header("Meus Dados (Profissional)")
        id_prof = st.session_state["usuario_id"]
        profissional = Service.profissional_listar_id(id_prof)
        
        if not profissional:
            st.error("Profissional não encontrado.")
            return

        nome = st.text_input("Nome", value=profissional.get_nome(), key="perfil_prof_nome")
        email = st.text_input("E-mail", value=profissional.get_email(), key="perfil_prof_email")
        especialidade = st.text_input("Especialidade", value=profissional.get_especialidade(), key="perfil_prof_esp")
        senha = st.text_input("Senha", type="password", value=profissional.get_senha(), key="perfil_prof_senha")

        if st.button("Atualizar Perfil", key="btn_perfil_prof"):
            try:
                Service.profissional_atualizar(id_prof, nome, email, especialidade, senha)
                st.success("Dados atualizados com sucesso!")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(erro)
            except Exception as e:
                st.error(f"Erro inesperado: {e}")