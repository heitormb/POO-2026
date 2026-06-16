from datetime import datetime, timedelta

# ==============================================================================
# Questão 1. Escrever a classe do modelo: Treino
# ==============================================================================
class Treino:
    def __init__(self, id, dt, ds, t):
        self.set_id(id)
        self.set_data(dt)
        self.set_distancia(ds)
        self.set_tempo(t)

    # Métodos Setters com as validações
    def set_id(self, id):
        if id < 0: raise ValueError("Id não pode ser negativo.")
        self.__id = id

    def set_data(self, dt):
        if dt > datetime.now(): raise ValueError("A data do treino não pode estar no futuro.")
        self.__data = dt

    def set_distancia(self, ds):
        if ds <= 0: raise ValueError("A distância deve ser maior que zero.")
        self.__distancia = ds

    def set_tempo(self, t):
        if t.total_seconds() <= 0: raise ValueError("O tempo deve ser maior que zero.")
        self.__tempo = t

    # Métodos Getters
    def get_id(self): return self.__id
    def get_data(self): return self.__data
    def get_distancia(self): return self.__distancia
    def get_tempo(self): return self.__tempo

    # Calcula o ritmo médio (pace)
    def Pace(self):
        # Transforma o tempo total em segundos e divide pela distância percorrida
        segundos_por_km = self.__tempo.total_seconds() / self.__distancia
        return timedelta(seconds=int(segundos_por_km))

    # Método ToString para exibição do objeto
    def __str__(self):
        return f"{self.__id} - {self.__data.strftime('%d/%m/%Y')} - {self.__distancia}km - {self.__tempo} - Pace: {self.Pace()}"


# ==============================================================================
# Questão 2. Escrever a classe de interface com o usuário: TreinoUI
# ==============================================================================
class TreinoUI:
    __treinos = []

    @staticmethod
    def main():
        op = 0
        while op != 7:
            op = TreinoUI.menu()
            if op == 1: TreinoUI.inserir()
            if op == 2: TreinoUI.listar()
            if op == 3: TreinoUI.listar_Id()
            if op == 4: TreinoUI.atualizar()
            if op == 5: TreinoUI.excluir()
            if op == 6: TreinoUI.MaisRapido()

    @staticmethod
    def menu():
        print("1-Inserir, 2-Listar Todos, 3-Listar ID, 4-Atualizar, 5-Excluir, 6-Mais Rápido, 7-Fim")
        return int(input("Informe uma opção: "))

    @classmethod
    def inserir(cls):
        id = int(input("Informe o id: "))
        dt = datetime.strptime(input("Informe a data (dd/mm/aaaa): "), "%d/%m/%Y")
        ds = float(input("Informe a distância (em km): "))
        
        # Coleta horas, minutos e segundos para montar o timedelta do tempo
        h = int(input("Informe as horas: "))
        m = int(input("Informe os minutos: "))
        s = int(input("Informe os segundos: "))
        t = timedelta(hours=h, minutes=m, seconds=s)

        x = Treino(id, dt, ds, t)
        cls.__treinos.append(x)

    @classmethod
    def listar(cls):
        for x in cls.__treinos: 
            print(x)

    @classmethod
    def listar_Id(cls):
        id = int(input("Informe o id do treino que busca: "))
        for x in cls.__treinos:
            if x.get_id() == id: 
                print(x)

    @classmethod
    def atualizar(cls):
        for x in cls.__treinos: print(x)
        id = int(input("Informe o id do treino a ser atualizado: "))
        for x in cls.__treinos:
            if x.get_id() == id:
                dt = datetime.strptime(input("Informe a nova data (dd/mm/aaaa): "), "%d/%m/%Y")
                ds = float(input("Informe a nova distância (em km): "))
                
                h = int(input("Informe as novas horas: "))
                m = int(input("Informe os novos minutos: "))
                s = int(input("Informe os novos segundos: "))
                t = timedelta(hours=h, minutes=m, seconds=s)

                x.set_data(dt)
                x.set_distancia(ds)
                x.set_tempo(t)

    @classmethod
    def excluir(cls):
        for x in cls.__treinos: print(x)
        id = int(input("Informe o id do treino a ser excluído: "))
        for x in cls.__treinos:
            if x.get_id() == id:
                cls.__treinos.remove(x)

    @classmethod
    def MaisRapido(cls):
        if len(cls.__treinos) == 0:
            print("Nenhum treino cadastrado.")
            return
            
        # O treino mais rápido é aquele com o menor Pace (menos tempo por quilômetro)
        menor = cls.__treinos[0]
        for x in cls.__treinos:
            if x.Pace() < menor.Pace():
                menor = x
        print("Treino mais rápido:")
        print(menor)


# Executa o programa
TreinoUI.main()