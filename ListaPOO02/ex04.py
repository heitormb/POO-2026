class EntradaCinema:
    def __init__(self):
        self._dia = ""
        self._hora = 0

    def set_dia(self, dia):
        self._dia = dia.lower()

    def set_hora(self, hora):
        if 0 <= hora <= 23:
            self._hora = hora
        else:
            raise ValueError("Hora inválida (0-23).")

    def get_dia(self):
        return self._dia

    def get_hora(self):
        return self._hora

    def _valor_base(self):
        if self._dia in ["segunda", "terca", "terça", "quinta"]:
            return 16.0
        elif self._dia == "quarta":
            return 8.0
        elif self._dia in ["sexta", "sabado", "sábado", "domingo"]:
            return 20.0
        else:
            raise ValueError("Dia inválido.")

    def valor_inteira(self):
        base = self._valor_base()

        if self._dia == "quarta":
            return base

        if 17 <= self._hora <= 23:
            base *= 1.5

        return base

    def valor_meia(self):
        return self.valor_inteira() / 2


if __name__ == "__main__":
    entrada = EntradaCinema()

    entrada.set_dia("sexta")
    entrada.set_hora(20)

    print("Dia:", entrada.get_dia())
    print("Hora:", entrada.get_hora(), "h")
    print("Entrada inteira: R$", entrada.valor_inteira())
    print("Meia-entrada: R$", entrada.valor_meia())