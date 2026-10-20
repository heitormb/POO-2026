import streamlit as st
from service import Service
from datetime import datetime
import time

class RegistrarAtendimentoUI:
    @staticmethod
    def main():
        st.header("Registrar Atendimento")
        # Lista horários confirmados do profissional logado que ainda não possuem atendimento
        horarios = [h for h in Service.horario_listar_profissional(st.session_state["usuario_id"]) if h.get_confirmado() == True]
        
        if len(horarios) == 0:
            st.write("Nenhum horário confirmado para atendimento")
        else:
            horario = st.selectbox("Informe o horário agendado", horarios, key="reg_atend_horario")
            data = st.text_input("Data e Horário", horario.get_data().strftime("%d/%m/%Y %H:%M"), key="reg_atend_data")
            queixa = st.text_area("Queixa Principal", key="reg_atend_queixa")
            historico = st.text_area("Histórico de Saúde", key="reg_atend_hist")
            avaliacao = st.text_area("Avaliação Clínica", key="reg_atend_aval")
            prescricao = st.text_area("Prescrição de exames e medicamentos", key="reg_atend_presc")
            total = st.number_input("Valor Total (R$)", min_value=0.0, value=0.0, key="reg_atend_total")
            
            if st.button("Registrar Atendimento", key="btn_salvar_atendimento"):
                Service.atendimento_inserir_completo(
                    datetime.strptime(data, "%d/%m/%Y %H:%M"),
                    queixa,
                    historico,
                    avaliacao,
                    prescricao,
                    horario.get_id(),
                    total,
                    False
                )
                st.success("Atendimento registrado com sucesso")
                time.sleep(2)
                st.rerun()