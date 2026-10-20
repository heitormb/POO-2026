import streamlit as st
from service import Service

class LoginUI:
    @staticmethod
    def main():
        st.header("Entrar no Sistema")
        email = st.text_input("Informe o e-mail", key="login_email")
        senha = st.text_input("Informe a senha", type="password", key="login_senha")
        if st.button("Entrar", key="btn_login"):
            c = Service.cliente_autenticar(email, senha)
            if c is not None:
                st.session_state["usuario_id"] = c["id"]
                st.session_state["usuario_nome"] = c["nome"]
                st.session_state["usuario_tipo"] = "cliente"
                st.rerun()
            else:
                p = Service.profissional_autenticar(email, senha)
                if p is not None:
                    st.session_state["usuario_id"] = p["id"]
                    st.session_state["usuario_nome"] = p["nome"]
                    st.session_state["usuario_tipo"] = "profissional"
                    st.rerun()
                else:
                    st.write("E-mail ou senha inválidos")