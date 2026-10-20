import streamlit as st
import pandas as pd
from service import Service

class VisualizarMinhaAgendaUI:
    @staticmethod
    def main():
        st.header("Minha Agenda")
        horarios = Service.horario_listar_profissional(st.session_state["usuario_id"])
        if len(horarios) == 0:
            st.write("Nenhum horário cadastrado")
        else:
            dic = []
            for obj in horarios:
                cliente = Service.cliente_listar_id(obj.get_id_cliente())
                servico = Service.servico_listar_id(obj.get_id_servico())
                cliente_nome = cliente.get_nome() if cliente else "None"
                servico_descr = servico.get_descricao() if servico else "None"
                dic.append({
                    "id": obj.get_id(),
                    "data": obj.get_data(),
                    "confirmado": obj.get_confirmado(),
                    "cliente": cliente_nome,
                    "serviço": servico_descr
                })
            df = pd.DataFrame(dic)
            st.dataframe(df)