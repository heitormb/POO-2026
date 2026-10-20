import streamlit as st
import pandas as pd
import time
from service import Service

class ManterClienteUI:
    @staticmethod
    def main():
        st.header("Cadastro de Clientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterClienteUI.listar()
        with tab2: ManterClienteUI.inserir()
        with tab3: ManterClienteUI.atualizar()
        with tab4: ManterClienteUI.excluir()
        
    @staticmethod
    def listar():
        clientes = Service.cliente_listar()
        if len(clientes) == 0: st.write("Nenhum cliente cadastrado")
        else:
            list_dic = []
            for obj in clientes: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
            Service.convenio_listar()
            
    @staticmethod
    def inserir():
        nome = st.text_input("Informe o nome", key="cliente_inserir_nome")
        email = st.text_input("Informe o e-mail", key="cliente_inserir_email")
        fone = st.text_input("Informe o fone", key="cliente_inserir_fone")
        id_convenio = st.text_input("Informe o id convenio", key="cliente_inserir_convenio")
        senha = st.text_input("Informe a senha", type="password", key="cliente_inserir_senha")
        if st.button("Inserir", key="btn_inserir_cliente"):
            Service.cliente_inserir(nome, email, fone, id_convenio, senha)
            st.success("Cliente inserido com sucesso")
            time.sleep(2)
            st.rerun()
            
    @staticmethod
    def atualizar():
        clientes = Service.cliente_listar()
        if len(clientes) == 0: st.write("Nenhum cliente cadastrado")
        else:
            Service.convenio_listar()
            op = st.selectbox("Atualização de Clientes", clientes, key="cliente_select_atualizar")
            nome = st.text_input("Novo nome", op.get_nome(), key="cliente_atualizar_nome")
            email = st.text_input("Novo e-mail", op.get_email(), key="cliente_atualizar_email")
            fone = st.text_input("Novo fone", op.get_fone(), key="cliente_atualizar_fone")
            id_convenio = st.text_input("Novo id convenio", str(op.get_id_convenio()), key="cliente_atualizar_convenio")
            senha = st.text_input("Nova senha", op.get_senha(), type="password", key="cliente_atualizar_senha")
            if st.button("Atualizar", key="btn_atualizar_cliente"):
                id = op.get_id()
                Service.cliente_atualizar(id, nome, email, fone, id_convenio, senha)
                st.success("Cliente atualizado com sucesso")
                time.sleep(2)
                st.rerun()
                
    @staticmethod
    def excluir():
        Service.convenio_listar()
        clientes = Service.cliente_listar()
        if len(clientes) == 0: st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Exclusão de Clientes", clientes, key="cliente_select_excluir")
            if st.button("Excluir", key="btn_excluir_cliente"):
                id = op.get_id()
                Service.cliente_excluir(id)
                st.success("Cliente excluído com sucesso")
                time.sleep(2)
                st.rerun()