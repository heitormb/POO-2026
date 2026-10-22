import streamlit as st
import pandas as pd
from service import Service

class ListarHorariosConfirmadosHojeUI:
    @staticmethod
    def main():
        st.header("Horários Confirmados de Hoje")
        horarios = Service.horario_listar_confirmados_hoje()
        if len(horarios) == 0:
            st.write("Nenhum horário confirmado para hoje")
        else:
            dic = []
            for obj in horarios:
                cliente = Service.cliente_listar_id(obj.get_id_cliente())
                servico = Service.servico_listar_id(obj.get_id_servico())
                profissional = Service.profissional_listar_id(obj.get_id_profissional())
                
                cliente_nome = cliente.get_nome() if cliente else "None"
                servico_descr = servico.get_descricao() if servico else "None"
                profissional_nome = profissional.get_nome() if profissional else "None"
                
                dic.append({"id": obj.get_id(), "data": obj.get_data().strftime("%d/%m/%Y %H:%M"), "cliente": cliente_nome, "serviço": servico_descr, "profissional": profissional_nome})
            df = pd.DataFrame(dic)
            st.dataframe(df)