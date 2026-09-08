import streamlit as st
from datetime import datetime
from service import Service

class ManterAtendimentoUI:
    @staticmethod
    def main():
        st.header("Cadastro de Atendimentos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with tab1:
            ManterAtendimentoUI.listar()
        with tab2:
            ManterAtendimentoUI.inserir()
        with tab3:
            ManterAtendimentoUI.atualizar()
        with tab4:
            ManterAtendimentoUI.excluir()

    @staticmethod
    def listar():
        atendimentos = Service.atendimento_listar()
        if len(atendimentos) == 0:
            st.write("Nenhum atendimento cadastrado.")
        else:
            dados = []
            for a in atendimentos:
                dt = a.get_data()
                data_str = dt.strftime("%d/%m/%Y %H:%M") if isinstance(dt, datetime) else str(dt)
                dados.append({
                    "ID": a.get_id(),
                    "Data": data_str,
                    "Queixa Principal": a.get_queixa_principal(),
                    "Histórico de Saúde": a.get_historico_saude(),
                    "Avaliação": a.get_avaliacao(),
                    "Prescrição": a.get_prescricao(),
                    "ID Horário": a.get_id_horario()
                })
            st.dataframe(dados)

    @staticmethod
    def inserir():
        data = st.date_input("Data do Atendimento")
        hora = st.time_input("Hora do Atendimento")
        queixa = st.text_input("Queixa Principal")
        historico = st.text_area("Histórico de Saúde")
        avaliacao = st.text_area("Avaliação")
        prescricao = st.text_area("Prescrição")
        id_horario = st.number_input("ID do Horário", min_value=1, step=1)

        if st.button("Inserir Atendimento"):
            dt_completa = datetime.combine(data, hora)
            # O ID é gerado automaticamente pelo DAO
            Service.atendimento_inserir(0, dt_completa, queixa, historico, avaliacao, prescricao, id_horario)
            st.success("Atendimento inserido com sucesso!")

    @staticmethod
    def atualizar():
        atendimentos = Service.atendimento_listar()
        if not atendimentos:
            st.write("Nenhum atendimento para atualizar.")
            return

        opcoes = {f"{a.get_id()} - {a.get_queixa_principal()}": a for a in atendimentos}
        selecionado = st.selectbox("Selecione o Atendimento para Atualizar", list(opcoes.keys()))

        if selecionado:
            atendimento = opcoes[selecionado]
            dt_orig = atendimento.get_data() if isinstance(atendimento.get_data(), datetime) else datetime.now()

            data = st.date_input("Data", value=dt_orig.date())
            hora = st.time_input("Hora", value=dt_orig.time())
            queixa = st.text_input("Queixa Principal", value=atendimento.get_queixa_principal())
            historico = st.text_area("Histórico de Saúde", value=atendimento.get_historico_saude())
            avaliacao = st.text_area("Avaliação", value=atendimento.get_avaliacao())
            prescricao = st.text_area("Prescrição", value=atendimento.get_prescricao())
            id_horario = st.number_input("ID do Horário", value=atendimento.get_id_horario(), min_value=1, step=1)

            if st.button("Atualizar Atendimento"):
                dt_completa = datetime.combine(data, hora)
                Service.atendimento_atualizar(atendimento.get_id(), dt_completa, queixa, historico, avaliacao, prescricao, id_horario)
                st.success("Atendimento atualizado com sucesso!")

    @staticmethod
    def excluir():
        atendimentos = Service.atendimento_listar()
        if not atendimentos:
            st.write("Nenhum atendimento para excluir.")
            return

        opcoes = {f"{a.get_id()} - {a.get_queixa_principal()}": a for a in atendimentos}
        selecionado = st.selectbox("Selecione o Atendimento para Excluir", list(opcoes.keys()))

        if selecionado:
            atendimento = opcoes[selecionado]
            if st.button("Excluir Atendimento"):
                Service.atendimento_excluir(atendimento.get_id())
                st.success("Atendimento excluído com sucesso!")