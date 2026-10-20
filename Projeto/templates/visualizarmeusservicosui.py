import streamlit as st
import pandas as pd
from service import Service

class VisualizarMeusServicosUI:
    @staticmethod
    def main():
        st.header("Meus Serviços")
        horarios = Service.horario_listar_cliente(st.session_state["usuario_id"])
        if len(horarios) == 0:
            st.write("Nenhum serviço agendado")
        else:
            dic = []
            for obj in horarios:
                profissional = Service.profissional_listar_id(obj.get_id_profissional())
                servico = Service.servico_listar_id(obj.get_id_servico())
                profissional_nome = profissional.get_nome() if profissional else "None"
                servico_descr = servico.get_descricao() if servico else "None"
                dic.append({
                    "id": obj.get_id(),
                    "data": obj.get_data(),
                    "confirmado": obj.get_confirmado(),
                    "serviço": servico_descr,
                    "profissional": profissional_nome
                })
            df = pd.DataFrame(dic)
            st.dataframe(df)