import streamlit as st
from templates.manterclienteui import ManterClienteUI
from templates.manteratendimentoui import ManterAtendimentoUI

class IndexUI:
    @staticmethod
    def main():
        st.sidebar.title("Menu")
        opcao = st.sidebar.selectbox("Selecione uma opção", ["Manter Clientes", "Manter Atendimentos"])

        if opcao == "Manter Clientes":
            ManterClienteUI.main()
        elif opcao == "Manter Atendimentos":
            ManterAtendimentoUI.main()

IndexUI.main()