import streamlit as st
import pandas as pd
import time
from service import Service

class ManterProfissionalUI:
    @staticmethod
    def main():
        st.header("Cadastro de Profissionais")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterProfissionalUI.listar()
        with tab2: ManterProfissionalUI.inserir()
        with tab3: ManterProfissionalUI.atualizar()
        with tab4: ManterProfissionalUI.excluir()

    @staticmethod
    def listar():
        profissionais = Service.profissional_listar()
        if len(profissionais) == 0: 
            st.write("Nenhum profissional cadastrado")
        else:
            list_dic = []
            for obj in profissionais: 
                d = obj.to_json()
                d.pop("senha", None)  # Ocultar senha na listagem por segurança
                list_dic.append(d)
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    @staticmethod
    def inserir():
        nome = st.text_input("Informe o nome", key="prof_inserir_nome")
        email = st.text_input("Informe o e-mail", key="prof_inserir_email")
        especialidade = st.text_input("Informe a especialidade", key="prof_inserir_esp")
        senha = st.text_input("Informe a senha", type="password", key="prof_inserir_senha")
        if st.button("Inserir", key="btn_inserir_prof"):
            Service.profissional_inserir(nome, email, especialidade, senha)
            st.success("Profissional inserido com sucesso")
            time.sleep(2)
            st.rerun()

    @staticmethod
    def atualizar():
        profissionais = Service.profissional_listar()
        if len(profissionais) == 0: 
            st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Atualização de Profissionais", profissionais, key="prof_select_atualizar")
            nome = st.text_input("Novo nome", op.get_nome(), key="prof_atualizar_nome")
            email = st.text_input("Novo e-mail", op.get_email(), key="prof_atualizar_email")
            especialidade = st.text_input("Nova especialidade", op.get_especialidade(), key="prof_atualizar_esp")
            senha = st.text_input("Nova senha", op.get_senha(), type="password", key="prof_atualizar_senha")
            if st.button("Atualizar", key="btn_atualizar_prof"):
                id = op.get_id()
                Service.profissional_atualizar(id, nome, email, especialidade, senha)
                st.success("Profissional atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    @staticmethod
    def excluir():
        profissionais = Service.profissional_listar()
        if len(profissionais) == 0: 
            st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Exclusão de Profissionais", profissionais, key="prof_select_excluir")
            if st.button("Excluir", key="btn_excluir_prof"):
                id = op.get_id()
                Service.profissional_excluir(id)
                st.success("Profissional excluído com sucesso")
                time.sleep(2)
                st.rerun()