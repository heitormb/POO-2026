import streamlit as st
import pandas as pd
from service import Service
import time

class ManterProfissionalUI:
    @staticmethod
    def main():
        st.header("Cadastro de Profissionais")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with tab1:
            ManterProfissionalUI.listar()
        with tab2:
            ManterProfissionalUI.inserir()
        with tab3:
            ManterProfissionalUI.atualizar()
        with tab4:
            ManterProfissionalUI.excluir()

    @staticmethod
    def listar():
        profissionais = Service.profissional_listar()
        if len(profissionais) == 0:
            st.write("Nenhum profissional cadastrado.")
        else:
            dic = []
            for p in profissionais:
                dic.append({
                    "id": p.get_id(),
                    "nome": p.get_nome(),
                    "email": p.get_email(),
                    "especialidade": p.get_especialidade()
                })
            df = pd.DataFrame(dic)
            st.dataframe(df)

    @staticmethod
    def inserir():
        nome = st.text_input("Informe o nome", key="prof_ins_nome")
        email = st.text_input("Informe o e-mail", key="prof_ins_email")
        especialidade = st.text_input("Informe a especialidade", key="prof_ins_esp")
        senha = st.text_input("Informe a senha", type="password", key="prof_ins_senha")

        if st.button("Inserir Profissional", key="btn_ins_prof"):
            try:
                Service.profissional_inserir(nome, email, especialidade, senha)
                st.success("Profissional inserido com sucesso!")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(erro)
            except Exception as e:
                st.error(f"Erro inesperado: {e}")

    @staticmethod
    def atualizar():
        profissionais = Service.profissional_listar()
        if len(profissionais) == 0:
            st.write("Nenhum profissional para atualizar.")
            return
        profissional = st.selectbox("Selecione o profissional", profissionais, key="prof_alt_sel")
        
        nome = st.text_input("Novo nome", value=profissional.get_nome(), key="prof_alt_nome")
        email = st.text_input("Novo e-mail", value=profissional.get_email(), key="prof_alt_email")
        especialidade = st.text_input("Nova especialidade", value=profissional.get_especialidade(), key="prof_alt_esp")
        senha = st.text_input("Nova senha", type="password", value=profissional.get_senha(), key="prof_alt_senha")

        if st.button("Atualizar Profissional", key="btn_alt_prof"):
            try:
                Service.profissional_atualizar(profissional.get_id(), nome, email, especialidade, senha)
                st.success("Profissional atualizado com sucesso!")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(erro)
            except Exception as e:
                st.error(f"Erro inesperado: {e}")

    @staticmethod
    def excluir():
        profissionais = Service.profissional_listar()
        if len(profissionais) == 0:
            st.write("Nenhum profissional para excluir.")
            return
        profissional = st.selectbox("Selecione o profissional para excluir", profissionais, key="prof_exc_sel")
        if st.button("Excluir Profissional", key="btn_exc_prof"):
            try:
                Service.profissional_excluir(profissional.get_id())
                st.success("Profissional excluído com sucesso!")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(erro)
            except Exception as e:
                st.error(f"Erro inesperado: {e}")