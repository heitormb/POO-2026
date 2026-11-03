import streamlit as st
import pandas as pd
from service import Service
import time

class ManterClienteUI:
    @staticmethod
    def main():
        st.header("Cadastro de Clientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with tab1:
            ManterClienteUI.listar()
        with tab2:
            ManterClienteUI.inserir()
        with tab3:
            ManterClienteUI.atualizar()
        with tab4:
            ManterClienteUI.excluir()

    @staticmethod
    def listar():
        clientes = Service.cliente_listar()
        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado.")
        else:
            dic = []
            for c in clientes:
                convenio = Service.convenio_listar_id(c.get_id_convenio())
                convenio_nome = convenio.get_nome() if convenio else "Nenhum"
                dic.append({
                    "id": c.get_id(),
                    "nome": c.get_nome(),
                    "email": c.get_email(),
                    "fone": c.get_fone(),
                    "convênio": convenio_nome
                })
            df = pd.DataFrame(dic)
            st.dataframe(df)

    @staticmethod
    def inserir():
        nome = st.text_input("Informe o nome", key="cli_ins_nome")
        email = st.text_input("Informe o e-mail", key="cli_ins_email")
        fone = st.text_input("Informe o fone", key="cli_ins_fone")
        senha = st.text_input("Informe a senha", type="password", key="cli_ins_senha")
        
        convenios = Service.convenio_listar()
        convenio = st.selectbox("Convênio", convenios, key="cli_ins_conv") if convenios else None
        id_convenio = convenio.get_id() if convenio else 1

        if st.button("Inserir Cliente", key="btn_ins_cli"):
            try:
                Service.cliente_inserir(nome, email, fone, id_convenio, senha)
                st.success("Cliente inserido com sucesso!")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(erro)
            except Exception as e:
                st.error(f"Erro inesperado: {e}")

    @staticmethod
    def atualizar():
        clientes = Service.cliente_listar()
        if len(clientes) == 0:
            st.write("Nenhum cliente para atualizar.")
            return
        cliente = st.selectbox("Selecione o cliente", clientes, key="cli_alt_sel")
        
        nome = st.text_input("Novo nome", value=cliente.get_nome(), key="cli_alt_nome")
        email = st.text_input("Novo e-mail", value=cliente.get_email(), key="cli_alt_email")
        fone = st.text_input("Novo fone", value=cliente.get_fone(), key="cli_alt_fone")
        senha = st.text_input("Nova senha", type="password", value=cliente.get_senha(), key="cli_alt_senha")
        
        convenios = Service.convenio_listar()
        convenio = st.selectbox("Convênio", convenios, index=next((i for i, c in enumerate(convenios) if c.get_id() == cliente.get_id_convenio()), 0) if convenios else 0, key="cli_alt_conv")
        id_convenio = convenio.get_id() if convenio else 1

        if st.button("Atualizar Cliente", key="btn_alt_cli"):
            try:
                Service.cliente_atualizar(cliente.get_id(), nome, email, fone, id_convenio, senha)
                st.success("Cliente atualizado com sucesso!")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(erro)
            except Exception as e:
                st.error(f"Erro inesperado: {e}")

    @staticmethod
    def excluir():
        clientes = Service.cliente_listar()
        if len(clientes) == 0:
            st.write("Nenhum cliente para excluir.")
            return
        cliente = st.selectbox("Selecione o cliente para excluir", clientes, key="cli_exc_sel")
        if st.button("Excluir Cliente", key="btn_exc_cli"):
            try:
                Service.cliente_excluir(cliente.get_id())
                st.success("Cliente excluído com sucesso!")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(erro)
            except Exception as e:
                st.error(f"Erro inesperado: {e}")