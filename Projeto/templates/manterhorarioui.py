import streamlit as st
import pandas as pd
from service import Service
from datetime import datetime
import time

class ManterHorarioUI:
    @staticmethod
    def main():
        st.header("Cadastro de Horários")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with tab1:
            ManterHorarioUI.listar()
        with tab2:
            ManterHorarioUI.inserir()
        with tab3:
            ManterHorarioUI.atualizar()
        with tab4:
            ManterHorarioUI.excluir()

    @staticmethod
    def listar():
        horarios = Service.horario_listar()
        if len(horarios) == 0:
            st.write("Nenhum horário cadastrado.")
        else:
            dic = []
            for h in horarios:
                dic.append({
                    "id": h.get_id(),
                    "data": h.get_data().strftime("%d/%m/%Y %H:%M"),
                    "confirmado": h.get_confirmado(),
                    "cliente": h.get_id_cliente(),
                    "serviço": h.get_id_servico(),
                    "profissional": h.get_id_profissional()
                })
            df = pd.DataFrame(dic)
            st.dataframe(df)

    @staticmethod
    def inserir():
        data_str = st.text_input("Data e Hora (dd/mm/aaaa HH:MM)", key="horario_ins_data")
        profissionais = Service.profissional_listar()
        servicos = Service.servico_listar()
        
        prof = st.selectbox("Profissional", profissionais, key="horario_ins_prof")
        serv = st.selectbox("Serviço", servicos, key="horario_ins_serv")

        if st.button("Inserir Horário", key="btn_ins_horario"):
            try:
                data = datetime.strptime(data_str, "%d/%m/%Y %H:%M")
                Service.horario_inserir(data, False, None, serv.get_id() if serv else None, prof.get_id() if prof else None)
                st.success("Horário inserido com sucesso!")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(erro)
            except Exception as e:
                st.error(f"Erro: {e}")

    @staticmethod
    def atualizar():
        horarios = Service.horario_listar()
        if len(horarios) == 0:
            st.write("Nenhum horário para atualizar.")
            return
        horario = st.selectbox("Selecione o horário", horarios, key="horario_alt_sel")
        data_str = st.text_input("Nova Data e Hora (dd/mm/aaaa HH:MM)", value=horario.get_data().strftime("%d/%m/%Y %H:%M"), key="horario_alt_data")
        confirmado = st.checkbox("Confirmado", value=horario.get_confirmado(), key="horario_alt_conf")
        
        profissionais = Service.profissional_listar()
        servicos = Service.servico_listar()
        clientes = Service.cliente_listar()

        prof = st.selectbox("Profissional", profissionais, index=next((i for i, p in enumerate(profissionais) if p.get_id() == horario.get_id_profissional()), 0), key="horario_alt_prof")
        serv = st.selectbox("Serviço", servicos, index=next((i for i, s in enumerate(servicos) if s.get_id() == horario.get_id_servico()), 0) if horario.get_id_servico() else 0, key="horario_alt_serv")
        cli = st.selectbox("Cliente", [None] + clientes, key="horario_alt_cli")

        if st.button("Atualizar Horário", key="btn_alt_horario"):
            try:
                data = datetime.strptime(data_str, "%d/%m/%Y %H:%M")
                id_cli = cli.get_id() if cli else None
                Service.horario_atualizar(horario.get_id(), data, confirmado, id_cli, serv.get_id() if serv else None, prof.get_id() if prof else None)
                st.success("Horário atualizado com sucesso!")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(erro)
            except Exception as e:
                st.error(f"Erro: {e}")

    @staticmethod
    def excluir():
        horarios = Service.horario_listar()
        if len(horarios) == 0:
            st.write("Nenhum horário para excluir.")
            return
        horario = st.selectbox("Selecione o horário para excluir", horarios, key="horario_exc_sel")
        if st.button("Excluir Horário", key="btn_exc_horario"):
            try:
                Service.horario_excluir(horario.get_id())
                st.success("Horário excluído com sucesso!")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(erro)
            except Exception as e:
                st.error(f"Erro: {e}")