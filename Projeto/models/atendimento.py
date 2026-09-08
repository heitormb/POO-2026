from datetime import datetime

class Atendimento:
    def __init__(self, id: int, data: datetime, queixa_principal: str, historico_saude: str, avaliacao: str, prescricao: str, id_horario: int):
        self.__id = id
        self.__data = data
        self.__queixa_principal = queixa_principal
        self.__historico_saude = historico_saude
        self.__avaliacao = avaliacao
        self.__prescricao = prescricao
        self.__id_horario = id_horario

    # Getters
    def get_id(self):
        return self.__id

    def get_data(self):
        return self.__data

    def get_queixa_principal(self):
        return self.__queixa_principal

    def get_historico_saude(self):
        return self.__historico_saude

    def get_avaliacao(self):
        return self.__avaliacao

    def get_prescricao(self):
        return self.__prescricao

    def get_id_horario(self):
        return self.__id_horario

    # Setters
    def set_id(self, id):
        self.__id = id

    def set_data(self, data):
        self.__data = data

    def set_queixa_principal(self, queixa_principal):
        self.__queixa_principal = queixa_principal

    def set_historico_saude(self, historico_saude):
        self.__historico_saude = historico_saude

    def set_avaliacao(self, avaliacao):
        self.__avaliacao = avaliacao

    def set_prescricao(self, prescricao):
        self.__prescricao = prescricao

    def set_id_horario(self, id_horario):
        self.__id_horario = id_horario

    def __str__(self):
        data_str = self.__data.strftime("%d/%m/%Y %H:%M") if isinstance(self.__data, datetime) else str(self.__data)
        return f"ID: {self.__id} | Data: {data_str} | Queixa: {self.__queixa_principal} | Histórico: {self.__historico_saude} | Avaliação: {self.__avaliacao} | Prescrição: {self.__prescricao} | ID Horário: {self.__id_horario}"