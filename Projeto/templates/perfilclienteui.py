import streamlit as st
from service import Service
import time

class PerfilClienteUI:
    @staticmethod
    def main():
        st.header("Meus Dados")
        id_cliente = st.session_state["usuario_id"]
        cliente = Service.cliente_listar_id(id_cliente)
        
        if not cliente:
            st.error("Cliente não encontrado.")
            return

        nome = st.text_input("Nome", value=cliente.get_nome(), key="perfil_cli_nome")
        email = st.text_input("E-mail", value=cliente.get_email(), key="perfil_cli_email")
        fone = st.text_input("Fone", value=cliente.get_fone(), key="perfil_cli_fone")
        senha = st.text_input("Senha", type="password", value=cliente.get_senha(), key="perfil_cli_senha")
        
        convenios = Service.convenio_listar()
        convenio = st.selectbox("Convênio", convenios, index=next((i for i, c in enumerate(convenios) if c.get_id() == cliente.get_id_convenio()), 0) if convenios else 0, key="perfil_cli_conv")
        id_convenio = convenio.get_id() if convenio else 1

        if st.button("Atualizar Perfil", key="btn_perfil_cli"):
            try:
                Service.cliente_atualizar(id_cliente, nome, email, fone, id_convenio, senha)
                st.success("Dados atualizados com sucesso!")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(erro)
            except Exception as e:
                st.error(f"Erro inesperado: {e}")