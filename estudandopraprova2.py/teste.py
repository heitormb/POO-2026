class Gyat:
    def __init__(self, rizz, sahur):
        self.set_rizz(rizz)
        self.set_sahur(sahur)

    def set_rizz(self, rizz):
        if rizz<0: raise ValueError("Betinha nao tem aura")
        self.rizz = rizz

    def set_sahur(self, sahur):
        if sahur == "": raise ValueError("triple t tem que ter nome seu beta")
        self.sahur = sahur
        
    def get_rizz(self):
        return self.rizz
    
    def get_sahur(self):
        return self.sahur
    
    def __str__(self):
        return f"{self.rizz} - {self.sahur}"
    
class UI:
    gyats=[]

    @staticmethod
    def main():
        op = 0

        while op != 5:
            op = UI.menu()

            if op == 1: UI.inserir()
            if op == 2: UI.listar()
            if op == 3: UI.atualizar()
            if op == 4: UI.excluir()

    @staticmethod
    def menu():
        print("1-inserir 2-listar 3-atualizar 4-excluir 5-fim")
        return int(input("escolha uma skibidi opçao:"))
    
    @classmethod
    def inserir(cls):
        rizz = int(input("informe seu rizz: "))
        sahur = input("fale o nome do seu tung tung: ")

        x = Gyat(rizz, sahur)
        cls.gyats.append(x)

        print("gyat inserida com sucesso")

    @classmethod
    def listar(cls):
        if len(cls.gyats) == 0:
            print("Nenhum gyat cadastrado")

        else:
            for x in cls.gyats:
                print(x)

    @classmethod
    def atualizar(cls):
        UI.listar()

        rizz = int(input("informe seu rizz:"))

        x = UI.listarrizz(rizz)

        if x != None:
            cls.gyats.remove(x)

            
            sahur = input("Informe o novo nome: ")

            novo = Gyat(rizz, sahur)

            cls.gyats.append(novo)

            print("gyat atualizada")

        else:
            print("gyat não encontrado")

        
    @classmethod
    def excluir(cls):
        UI.listar()

        rizz = int(input("informe seu rizz:"))

        x = UI.listarrizz(rizz)

        if x != None:
            cls.gyats.remove(x)


    @classmethod
    def listarrizz(cls, rizz):
        for x in cls.gyats:
            if x.get_rizz() == rizz:
                return x

        return None




UI.main()
