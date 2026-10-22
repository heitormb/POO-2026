import streamlit as st
import pandas as pd
from service import Service

class ListarAgendaProfissionalUI:
    @staticmethod
    def main():
        st.header("Listar Agenda do Profissional")
        profissionais = Service.profissional_listar()
        if len(profissionais) == 0:
            st.write("Nenhum profissional cadastrado")
        else:
            profissional = st.selectbox("Selecione o Profissional", profissionais, key="select_agenda_prof")
            if profissional:
                horarios = Service.horario_listar_por_profissional(profissional.get_id())
                if len(horarios) == 0:
                    st.write("Nenhum horário encontrado para este profissional")
                else:
                    dic = []
                    for obj in horarios:
                        cliente = Service.cliente_listar_id(obj.get_id_cliente())
                        servico = Service.servico_listar_id(obj.get_id_servico())
                        
                        cliente_nome = cliente.get_nome() if cliente else "None"
                        servico_descr = servico.get_descricao() if servico else "None"
                        
                        dic.append({"id": obj.get_id(), "data": obj.get_data().strftime("%d/%m/%Y %H:%M"), "cliente": cliente_nome, "serviço": servico_descr})
                    df = pd.DataFrame(dic)
                    st.dataframe(df)