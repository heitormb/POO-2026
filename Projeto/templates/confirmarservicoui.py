import streamlit as st
from service import Service
import time

class ConfirmarServicoUI:
    @staticmethod
    def main():
        st.header("Confirmar Serviço")
        horarios = Service.horario_listar_pendentes(st.session_state["usuario_id"])
        if len(horarios) == 0:
            st.write("Nenhum serviço pendente de confirmação")
        else:
            horario = st.selectbox("Informe o horário", horarios, key="conf_horario")
            cliente = Service.cliente_listar_id(horario.get_id_cliente())
            if cliente:
                st.write(f"Cliente: {cliente.get_nome()} - {cliente.get_email()} - {cliente.get_fone()}")
            if st.button("Confirmar", key="btn_confirmar_servico"):
                Service.horario_atualizar(
                    horario.get_id(),
                    horario.get_data(),
                    True,
                    horario.get_id_cliente(),
                    horario.get_id_servico(),
                    horario.get_id_profissional()
                )
                st.success("Serviço confirmado com sucesso")
                time.sleep(2)
                st.rerun()