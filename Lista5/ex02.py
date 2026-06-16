from datetime import datetime
from enum import Enum

# ==============================================================================
# Enumeração para as situações de pagamento
# ==============================================================================
class Pagamento(Enum):
    EmAberto = 1
    PagoParcial = 2
    Pago = 3


# ==============================================================================
# Classe do modelo: Boleto
# ==============================================================================
class Boleto:
    def __init__(self, cod, emissao, venc, valor):
        self.set_codBarras(cod)
        self.set_dateEmissao(emissao)
        self.set_dataVencimento(venc)
        self.set_valorBoleto(valor)
        self.__dataPagto = None
        self.__valorPago = 0.0

    # Métodos Setters com as validações
    def set_codBarras(self, cod):
        if cod == "": raise ValueError("Código de barras não pode ser vazio.")
        self.__codBarras = cod

    def set_dateEmissao(self, emissao):
        self.__dateEmissao = emissao

    def set_dataVencimento(self, venc):
        if venc < self.__dateEmissao: raise ValueError("Vencimento inválido.")
        self.__dataVencimento = venc

    def set_valorBoleto(self, valor):
        if valor <= 0: raise ValueError("Valor deve ser maior que zero.")
        self.__valorBoleto = valor

    def set_dataPagto(self, dataPagto):
        self.__dataPagto = dataPagto

    def set_valorPago(self, valorPago):
        if valorPago < 0: raise ValueError("Valor pago inválido.")
        self.__valorPago = valorPago

    # Métodos Getters
    def get_codBarras(self): return self.__codBarras
    def get_dateEmissao(self): return self.__dateEmissao
    def get_dataVencimento(self): return self.__dataVencimento
    def get_dataPagto(self): return self.__dataPagto
    def get_valorBoleto(self): return self.__valorBoleto
    def get_valorPago(self): return self.__valorPago

    # Método Pagar
    def Pagar(self, valorPago):
        if valorPago <= 0: raise ValueError("Valor deve ser maior que zero.")
        if valorPago > self.__valorBoleto: raise ValueError("Valor maior que o boleto.")
        self.set_valorPago(valorPago)
        self.set_dataPagto(datetime.now())

    # Método Situacao
    def Situacao(self):
        if self.__valorPago == 0: return Pagamento.EmAberto
        if self.__valorPago < self.__valorBoleto: return Pagamento.PagoParcial
        return Pagamento.Pago

    # Método ToString sem NENHUMA operação ou if/else interno
    def __str__(self):
        return f"{self.__codBarras} - {self.__dateEmissao} - {self.__dataVencimento} - {self.__valorBoleto} - {self.__valorPago} - {self.__dataPagto} - {self.Situacao()}"


# ==============================================================================
# Classe de interface com o usuário: BoletoUI
# ==============================================================================
class BoletoUI:
    __boletos = []

    @staticmethod
    def main():
        op = 0
        while op != 10:
            try:
                op = BoletoUI.menu()
                if op == 1: BoletoUI.Inserir()
                if op == 2: BoletoUI.Listar()
                if op == 3: BoletoUI.Page_Atualizar()
                if op == 4: BoletoUI.Excluir()
                if op == 5: BoletoUI.BoletosEmAberto()
                if op == 6: BoletoUI.BoletosPagos()
                if op == 7: BoletoUI.BoletosAVencer()
                if op == 8: BoletoUI.BoletosVencidos()
                if op == 9: BoletoUI.PagarBoleto()
            except ValueError as e:
                print(f"Erro: {e}")

    @staticmethod
    def menu():
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 5-Em Aberto, 6-Pagos, 7-A Vencer, 8-Vencidos, 9-Pagar, 10-Fim")
        return int(input("Informe uma opção: "))

    @classmethod
    def Inserir(cls):
        cod = input("Código de barras: ")
        emissao = datetime.strptime(input("Emissão (dd/mm/aaaa): "), "%d/%m/%Y")
        venc = datetime.strptime(input("Vencimento (dd/mm/aaaa): "), "%d/%m/%Y")
        valor = float(input("Valor do boleto: "))
        x = Boleto(cod, emissao, venc, valor)
        cls.__boletos.append(x)

    @classmethod
    def Listar(cls):
        for x in cls.__boletos: print(x)

    @classmethod
    def Page_Atualizar(cls):
        for x in cls.__boletos: print(x)
        cod = input("Código do boleto a atualizar: ")
        for x in cls.__boletos:
            if x.get_codBarras() == cod:
                emissao = datetime.strptime(input("Nova data de emissão: "), "%d/%m/%Y")
                venc = datetime.strptime(input("Nova data de vencimento: "), "%d/%m/%Y")
                valor = float(input("Novo valor: "))
                x.set_dateEmissao(emissao)
                x.set_dataVencimento(venc)
                x.set_valorBoleto(valor)

    @classmethod
    def Excluir(cls):
        for x in cls.__boletos: print(x)
        cod = input("Código do boleto a excluir: ")
        for x in cls.__boletos:
            if x.get_codBarras() == cod:
                cls.__boletos.remove(x)

    @classmethod
    def BoletosEmAberto(cls):
        for x in cls.__boletos:
            if x.Situacao() == Pagamento.EmAberto: print(x)

    @classmethod
    def BoletosPagos(cls):
        for x in cls.__boletos:
            if x.Situacao() == Pagamento.Pago or x.Situacao() == Pagamento.PagoParcial: print(x)

    @classmethod
    def BoletosAVencer(cls):
        hoje = datetime.now()
        for x in cls.__boletos:
            if x.Situacao() == Pagamento.EmAberto and x.get_dataVencimento() >= hoje: print(x)

    @classmethod
    def BoletosVencidos(cls):
        hoje = datetime.now()
        for x in cls.__boletos:
            if x.Situacao() == Pagamento.EmAberto and x.get_dataVencimento() < hoje: print(x)

    @classmethod
    def PagarBoleto(cls):
        cod = input("Código do boleto a pagar: ")
        for x in cls.__boletos:
            if x.get_codBarras() == cod:
                valor = float(input("Valor a pagar: "))
                x.Pagar(valor)


BoletoUI.main()