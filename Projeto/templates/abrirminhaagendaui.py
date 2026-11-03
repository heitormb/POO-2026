import streamlit as st
from service import Service
from datetime import datetime, timedelta
import time

class AbrirMinhaAgendaUI:
    @staticmethod
    def main():
        st.header("Abrir Minha Agenda")
        data_str = st.text_input("Informe a data no formato dd/mm/aaaa", key="abrir_agenda_data")
        hora_ini_str = st.text_input("Informe o horário inicial no formato HH:MM", key="abrir_agenda_ini")
        hora_fim_str = st.text_input("Informe o horário final no formato HH:MM", key="abrir_agenda_fim")
        intervalo = st.number_input("Informe o intervalo entre os horários (min)", min_value=1, value=30, key="abrir_agenda_intervalo")

        if st.button("Abrir Agenda", key="btn_abrir_agenda"):
            try:
                data_base = datetime.strptime(data_str, "%d/%m/%Y").date()
                hora_ini = datetime.strptime(hora_ini_str, "%H:%M").time()
                hora_fim = datetime.strptime(hora_fim_str, "%H:%M").time()

                dt_atual = datetime.combine(data_base, hora_ini)
                dt_fim = datetime.combine(data_base, hora_fim)

                id_prof = st.session_state["usuario_id"]

                while dt_atual <= dt_fim:
                    Service.horario_inserir(dt_atual, False, None, None, id_prof)
                    dt_atual += timedelta(minutes=int(intervalo))

                st.success("Agenda aberta com sucesso!")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(f"Erro: {erro}")
            except Exception as e:
                st.error(f"Erro nos dados informados: {e}")