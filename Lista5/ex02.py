from datetime import datetime

class Pagamento:
    EM_ABERTO = 1
    PAGO_PARCIAL = 2
    PAGO = 3

class Boleto:
    def __init__(self, cod: str, emissao: datetime, venc: datetime, valor: float):
        self.set_codBarras(cod)
        self.set_dateEmissao(emissao)
        self.set_dataVencimento(venc)
        self.set_dataPagto(None) # Inicialmente sem data de pagamento
        self.set_valorBoleto(valor)
        self.set_valorPago(0.0) # Inicialmente nenhum valor foi pago
        self.set_situacaoPagamento(Pagamento.EM_ABERTO)

    def set_codBarras(self, cod):
        if cod == "": raise ValueError("Código de barras não pode ser vazio")
        self.__codBarras = cod

    def set_dateEmissao(self, emissao):
        self.__dateEmissao = emissao

    def set_dataVencimento(self, venc):
        if venc < self.__dateEmissao: raise ValueError("Vencimento não pode ser anterior à emissão")
        self.__dataVencimento = venc

    def set_dataPagto(self, data):
        self.__dataPagto = data

    def set_valorBoleto(self, valor):
        if valor <= 0: raise ValueError("Valor do boleto deve ser maior que zero")
        self.__valorBoleto = valor

    def set_valorPago(self, valor):
        if valor < 0: raise ValueError("Valor pago não pode ser negativo")
        self.__valorPago = valor

    def set_situacaoPagamento(self, situacao):
        self.__situacaoPagamento = situacao

    def get_codBarras(self): return self.__codBarras
    def get_dateEmissao(self): return self.__dateEmissao
    def get_dataVencimento(self): return self.__dataVencimento
    def get_dataPagto(self): return self.__dataPagto
    def get_valorBoleto(self): return self.__valorBoleto
    def get_valorPago(self): return self.__valorPago
    def get_situacaoPagamento(self): return self.__situacaoPagamento

    def Pagar(self, valorPago: float):
        if self.__situacaoPagamento == Pagamento.PAGO:
            raise ValueError("Este boleto já está totalmente pago")
        
        if valorPago <= 0:
            raise ValueError("O valor pago deve ser maior que zero")
            
        novo_total_pago = self.__valorPago + valorPago
        if novo_total_pago > self.__valorBoleto:
            raise ValueError("O valor total pago não pode ser maior que o valor do boleto")
            
        self.set_valorPago(novo_total_pago)
        self.set_dataPagto(datetime.now())
        
        if self.__valorPago == self.__valorBoleto:
            self.set_situacaoPagamento(Pagamento.PAGO)
        else:
            self.set_situacaoPagamento(Pagamento.PAGO_PARCIAL)

    def Situacao(self):
        if self.__situacaoPagamento == Pagamento.EM_ABERTO: return "Em Aberto"
        if self.__situacaoPagamento == Pagamento.PAGO_PARCIAL: return "Pago Parcial"
        if self.__situacaoPagamento == Pagamento.PAGO: return "Pago"

    def __str__(self):
        dt_venc = self.__dataVencimento.strftime("%d/%m/%Y")
        dt_pagto = self.__dataPagto.strftime("%d/%m/%Y") if self.__dataPagto else "Não pago"
        return f"Cód: {self.__codBarras} | Venc: {dt_venc} | Total: R${self.__valorBoleto:.2f} | Pago: R${self.__valorPago:.2f} | Status: {self.Situacao()} | Pago em: {dt_pagto}"


class BoletoUI:
    __boletos = []

    @staticmethod
    def main():
        op = 0
        while op != 11: # 11 é a opção Sair do menu
            op = BoletoUI.Menu()
            if op == 1: BoletoUI.Inserir()
            elif op == 2: BoletoUI.Listar()
            elif op == 3: BoletoUI.Atualizar()
            elif op == 4: BoletoUI.Excluir()
            elif op == 5: BoletoUI.BoletosEmAberto()
            elif op == 6: BoletoUI.BoletosPagos()
            elif op == 7: BoletoUI.BoletosAVencer()
            elif op == 8: BoletoUI.BoletosVencidos()
            elif op == 9: BoletoUI.PagarBoleto()

    @staticmethod
    def Menu():
        print("\n--- MENU BOLETOS ---")
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir")
        print("5-Em Aberto, 6-Pagos (Parcial/Total), 7-A Vencer, 8-Vencidos")
        print("9-Pagar Boleto, 11-Sair")
        try:
            return int(input("Informe uma opção: "))
        except ValueError:
            return 0

    @classmethod
    def Inserir(cls):
        print("\n--- Inserir Boleto ---")
        try:
            cod = input("Código de barras: ")
            emissao = datetime.strptime(input("Data de Emissão (dd/mm/aaaa): "), "%d/%m/%Y")
            venc = datetime.strptime(input("Data de Vencimento (dd/mm/aaaa): "), "%d/%m/%Y")
            valor = float(input("Valor do Boleto: R$ "))
            
            x = Boleto(cod, emissao, venc, valor)
            cls.__boletos.append(x)
            print("Boleto cadastrado com sucesso!")
        except Exception as e:
            print(f"Erro: {e}")

    @classmethod
    def Listar(cls):
        print("\n--- Todos os Boletos ---")
        if not cls.__boletos: print("Nenhum boleto cadastrado.")
        for x in cls.__boletos: print(x)

    @classmethod
    def Atualizar(cls):
        print("\n--- Atualizar Boleto ---")
        cod = input("Informe o código do boleto a ser atualizado: ")
        for x in cls.__boletos:
            if x.get_codBarras() == cod:
                try:
                    venc = datetime.strptime(input("Nova Data de Vencimento (dd/mm/aaaa): "), "%d/%m/%Y")
                    valor = float(input("Novo Valor do Boleto: R$ "))
                    x.set_dataVencimento(venc)
                    x.set_valorBoleto(valor)
                    print("Boleto atualizado com sucesso!")
                    return
                except Exception as e:
                    print(f"Erro: {e}")
                    return
        print("Boleto não encontrado.")

    @classmethod
    def Excluir(cls):
        print("\n--- Excluir Boleto ---")
        cod = input("Informe o código do boleto a ser excluído: ")
        for x in cls.__boletos:
            if x.get_codBarras() == cod:
                cls.__boletos.remove(x)
                print("Boleto removido com sucesso!")
                return
        print("Boleto não encontrado.")

    @classmethod
    def BoletosEmAberto(cls):
        print("\n--- Boletos em Aberto ---")
        cont = 0
        for x in cls.__boletos:
            if x.get_situacaoPagamento() == Pagamento.EM_ABERTO:
                print(x)
                cont += 1
        if cont == 0: print("Nenhum boleto em aberto.")

    @classmethod
    def BoletosPagos(cls):
        print("\n--- Boletos Pagos (Parcial ou Total) ---")
        cont = 0
        for x in cls.__boletos:
            if x.get_situacaoPagamento() in [Pagamento.PAGO_PARCIAL, Pagamento.PAGO]:
                print(x)
                cont += 1
        if cont == 0: print("Nenhum boleto pago.")

    @classmethod
    def BoletosAVencer(cls):
        print("\n--- Boletos a Vencer (Não pagos e dentro do prazo) ---")
        hoje = datetime.now()
        cont = 0
        for x in cls.__boletos:
            if x.get_situacaoPagamento() != Pagamento.PAGO and x.get_dataVencimento() >= hoje:
                print(x)
                cont += 1
        if cont == 0: print("Nenhum boleto a vencer encontrado.")

    @classmethod
    def BoletosVencidos(cls):
        print("\n--- Boletos Vencidos (Não pagos e fora do prazo) ---")
        hoje = datetime.now()
        cont = 0
        for x in cls.__boletos:
            if x.get_situacaoPagamento() != Pagamento.PAGO and x.get_dataVencimento() < hoje:
                print(x)
                cont += 1
        if cont == 0: print("Nenhum boleto vencido encontrado.")

    @classmethod
    def PagarBoleto(cls):
        print("\n--- Efetuar Pagamento de Boleto ---")
        cod = input("Informe o código do boleto: ")
        for x in cls.__boletos:
            if x.get_codBarras() == cod:
                try:
                    valor = float(input(f"Valor do boleto é R${x.get_valorBoleto():.2f} (Já pago: R${x.get_valorPago():.2f}). Informe o quanto vai pagar agora: R$ "))
                    x.Pagar(valor)
                    print("Pagamento registrado com sucesso!")
                    return
                except Exception as e:
                    print(f"Erro: {e}")
                    return
        print("Boleto não encontrado.")


BoletoUI.main()