import streamlit as st
from service import Service
from datetime import datetime, timedelta
import time

class AbrirMinhaAgendaUI:
    @staticmethod
    def main():
        st.header("Abrir Minha Agenda")
        data_str = st.text_input("Informe a data no formato dd/mm/aaaa", datetime.now().strftime("%d/%m/%Y"), key="abrir_agenda_data")
        hora_inicio_str = st.text_input("Informe o horário inicial no formato HH:MM", "09:00", key="abrir_agenda_inicio")
        hora_fim_str = st.text_input("Informe o horário final no formato HH:MM", "12:00", key="abrir_agenda_fim")
        intervalo = st.number_input("Informe o intervalo entre os horários (min)", min_value=1, value=30, key="abrir_agenda_intervalo")
        
        if st.button("Abrir Agenda", key="btn_abrir_agenda"):
            try:
                data_base = datetime.strptime(data_str, "%d/%m/%Y").date()
                h_inicio = datetime.strptime(hora_inicio_str, "%H:%M").time()
                h_fim = datetime.strptime(hora_fim_str, "%H:%M").time()
                
                dt_atual = datetime.combine(data_base, h_inicio)
                dt_fim = datetime.combine(data_base, h_fim)
                delta = timedelta(minutes=int(intervalo))
                
                while dt_atual <= dt_fim:
                    Service.horario_inserir(dt_atual, False, 0, 0, st.session_state["usuario_id"])
                    dt_atual += delta
                
                st.success("Agenda aberta com sucesso")
                time.sleep(2)
                st.rerun()
            except Exception as e:
                st.error(f"Erro ao abrir agenda: {e}")