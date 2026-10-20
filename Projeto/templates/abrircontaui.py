import streamlit as st
from service import Service
import time

class AbrirContaUI:
    @staticmethod
    def main():
        st.header("Abrir Conta no Sistema")
        nome = st.text_input("Informe o nome", key="abrir_conta_nome")
        email = st.text_input("Informe o e-mail", key="abrir_conta_email")
        fone = st.text_input("Informe o fone", key="abrir_conta_fone")
        senha = st.text_input("Informe a senha", type="password", key="abrir_conta_senha")
        
        if st.button("Inserir", key="btn_abrir_conta"):
            Service.cliente_inserir(nome, email, fone, 1, senha)
            st.success("Conta criada com sucesso")
            time.sleep(2)
            st.rerun()