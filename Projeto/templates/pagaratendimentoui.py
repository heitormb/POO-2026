import streamlit as st
import pandas as pd
from service import Service
import time

class PagarAtendimentoUI:
    @staticmethod
    def main():
        st.header("Pagar Atendimento")
        atendimentos = [a for a in Service.atendimento_listar_cliente(st.session_state["usuario_id"]) if a.get_pago() == False]
        
        if len(atendimentos) == 0:
            st.write("Nenhum atendimento pendente de pagamento")
        else:
            atendimento = st.selectbox("Selecione o atendimento para pagamento", atendimentos, key="pagar_atendimento_select")
            st.write(f"Valor Total a Pagar: R$ {atendimento.get_total():.2f}")
            
            if st.button("Efetuar Pagamento", key="btn_efetuar_pagamento"):
                Service.atendimento_atualizar(
                    atendimento.get_id(),
                    atendimento.get_data(),
                    atendimento.get_queixa_principal(),
                    atendimento.get_historico_saude(),
                    atendimento.get_avaliacao(),
                    atendimento.get_prescricao(),
                    atendimento.get_id_horario()
                )
                # Atualizando especificamente o status de pagamento
                atendimento.set_pago(True)
                Service.atendimento_atualizar(
                    atendimento.get_id(),
                    atendimento.get_data(),
                    atendimento.get_queixa_principal(),
                    atendimento.get_historico_saude(),
                    atendimento.get_avaliacao(),
                    atendimento.get_prescricao(),
                    atendimento.get_id_horario()
                )
                # Opcional: atualizar via dao direto se preferir, mas os setters cobrem. Vamos garantir salvando o objeto atualizado.
                st.success("Pagamento efetuado com sucesso! Atendimento finalizado.")
                time.sleep(2)
                st.rerun()