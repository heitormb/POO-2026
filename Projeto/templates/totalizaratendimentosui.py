import streamlit as st
import pandas as pd
from service import Service
from datetime import datetime, date

class TotalizarAtendimentosUI:
    @staticmethod
    def main():
        st.header("Totalizar Atendimentos dos Profissionais")
        
        col1, col2 = st.columns(2)
        with col1:
            data_inicio = st.date_input("Data Inicial", value=date.today(), key="tot_data_inicio")
        with col2:
            data_fim = st.date_input("Data Final", value=date.today(), key="tot_data_fim")
            
        if st.button("Totalizar", key="btn_totalizar"):
            if data_inicio > data_fim:
                st.error("A data inicial não pode ser maior que a data final.")
            else:
                dados = Service.atendimento_totalizar(data_inicio, data_fim)
                if len(dados) == 0:
                    st.write("Nenhum registro encontrado para o período.")
                else:
                    df = pd.DataFrame(dados)
                    st.dataframe(df)