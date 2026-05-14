class Componente:
    def __init__(self, id, nome, fabricante, valor):
        self.set_id(id)
        self.set_nome(nome)
        self.set_fabricante(fabricante)
        self.set_valor(valor)

    def set_id(self, id):
        if id<0: raise ValueError("seu buxa")
        self.id = id

    def set_nome(self, nome):
        if nome=="": raise ValueError("seu buxa")
        self.nome = nome

    def set_fabricante(self, fabricante):
        if fabricante=="": raise ValueError("seu buxa")
        self.fabricante = fabricante

    def set_valor(self, valor):
        if valor<0: raise ValueError("seu buxa")
        self.valor = valor

    def get_id(self):
        return self.id
    
    def get_nome(self):
        return self.nome
    
    def get_fabricante(self):
        return self.fabricante
    
    def get_valor(self):
        return self.valor
    
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.fabricante} - {self.valor}"
    

class UI:
    componentes=[]

    @staticmethod
    def main():
        op = 0

        while op!=4:
            op = UI.menu()

            if op==1:UI.inserir()
            if op==2:UI.listar()
            if op==3:UI.valor_total()

    @staticmethod
    def menu():
        print("1-inserir 2-listar 3-valor total 4-fim")
        return int(input("escolha uma opção: "))
    
    @classmethod
    def inserir(cls):
        id = int(input("informe o id: "))
        nome = input("informe o nome: ")
        fabricante = input("informe o fabricante: ")
        valor = float(input("informe o valor: "))

        x=Componente(id, nome, fabricante, valor)
        cls.componentes.append(x)
        print("componente inserido com sucesso")

    @classmethod
    def listar(cls):
        if len(cls.componentes) == 0:
            print("nenhum componente encontrado")
        else:
            for x in cls.componentes:
                print(x)

    @classmethod
    def valor_total(cls):
        if UI.verificar_valor()==0:
            print("a lista não tem componentes")
        else:
            print(UI.verificar_valor())

    @classmethod
    def verificar_valor(cls):
        valor=0
        for x in cls.componentes:
            soma = x.get_valor()
            valor += soma
        return valor
    

UI.main()