class Playlist:
    def __init__(self, id, nome, descricao):
        self.set_id(id)
        self.set_nome(nome)
        self.set_descricao(descricao)

        def set_id(self, id):
            if id<0:
                raise ValueError("O id deve ser positivo")
            self.id = id

        def set_nome(self, nome):
            if nome == "":
                raise ValueError("O nome não pode ser vazio")
            self.nome = nome

        def set_descricao(self, descricao):
            if nome == "":
                raise ValueError("a descrição não pode ser vazia")
            self.descricao = descricao

        def get_id(self):
            return self.id
        
        def get_nome(self):
            return self.nome
        
        def get_descricao(self):
            return self.descricao
        
        def __str__(self):
            return f"{self.id} - {self.nome} - {self.descricao}"
        

class Musica:
    def __init__(self, id, titulo, artista, album):
        self.set_id(id)
        self.set_titulo(titulo)
        self.set_artista(artista)
        self.set_album(album)

        def set_id(self, id):
            if id<0:
                raise ValueError("O id deve ser positivo")
            self.id = id

        def set_titulo(self, titulo):
            if titulo == "":
                raise ValueError("O titulo não pode ser vazio")
            self.titulo = titulo

        def set_artista(self, artista):
            if artista == "":
                raise ValueError("O artista não pode ser vazio")
            self.artista = artista
        
        def set_album(self, album):
            if album == "":
                raise ValueError("o álbum tem que ter nome")
            self.album = album

        

        def get_id(self):
            return self.id
        
        def get_titulo(self):
            return self.titulo
        
        def get_artista(self):
            return self.artista
        
        def get_album(self):
            return self.album
        
        def __str__(self):
            return f"{self.id} - {self.titulo} - {self.artista} - {self.album}"
        

class PlayListItem:
    def __init__(self, id, idplaylist, idmusica, sequencia):
        self.set_id(id)
        self.set_idplaylist(idplaylist)
        self.set_idmusica(idmusica)
        self.set_sequencia(sequencia)

        def set_id(self, id):
            if id<0:
                raise ValueError("id tem que ser maior que zero")
            self.id = id

        def set_idplaylist(self, idplaylist):
            if idplaylist<0:
                raise ValueError("id tem que ser maior que zero")
            self.idplaylist = idplaylist

        def set_idplaylist(self, idmusica):
            if idmusica<0:
                raise ValueError("id tem que ser maior que zero")
            self.idmusica = idmusica

        def set_sequencia(self, sequencia):
            if sequencia<0:
                raise ValueError("sequência tem que ser maior que zero")
            self.sequencia = sequencia

        def get_id(self):
            return self.id
        
        def get_idplaylist(self):
            return self.idplaylist
        
        def get_idmusica(self):
            return self.idmusica
        
        def get_sequencia(self):
            return self.sequencia
        
        def __str__(self):
            return f"{self.id} - {self.idplaylist} - {self.idmusica} - {self.sequencia}"
        

class UI:
    Playlist = []
    Musica = []
    PlayListItem = []

    @staticmethod
    def main():
        op = 0

        while op != 13:
            op = UI.menu()

            if op == 1:
                UI.inserir_playlist()

            elif op == 2:
                UI.listar_playlist()

            elif op == 3:
                UI.atualizar_playlist()

            elif op == 4:
                UI.excluir_playlist()

            elif op == 5:
                UI.inserir_musica()

            elif op == 6:
                UI.listar_musica()

            elif op == 7:
                UI.atualizar_musica()

            elif op == 8:
                UI.excluir_musica()

            elif op == 9:
                UI.inserir_item()

            elif op == 10:
                UI.listar_item()

            elif op == 11:
                UI.atualizar_item()

            elif op == 12:
                UI.excluir_item()

    @staticmethod
    def menu():
        print("\n1-Inserir playlist")
        print("2-Listar playlists")
        print("3-Atualizar playlist")
        print("4-Excluir playlist")
        print("5-Inserir música")
        print("6-Listar músicas")
        print("7-Atualizar música")
        print("8-Excluir música")
        print("9-Inserir item")
        print("10-Listar itens")
        print("11-Atualizar item")
        print("12-Excluir item")
        print("13-Fim")

        return int(input("Escolha uma opção: "))
    
    @classmethod
    def inserir_playlist(cls):
        id = int(input("Informe o id da playlist: "))
        nome = input("Informe o nome da playlist: ")
        descricao = input("Informe a descrição: ")

        x = Playlist(id, nome, descricao)

        cls.Playlist.append(x)

        print("aura farmada com sucesso")