class PlayList:
    def __init__(self, id, nome, descricao):
        self.set_id(id)
        self.set_nome(nome)
        self.set_descricao(descricao)

    def set_id(self, id):
        if id <= 0:
            raise ValueError("O id deve ser positivo")
        self.id = id

    def set_nome(self, nome):
        if nome == "":
            raise ValueError("O nome não pode ser vazio")
        self.nome = nome

    def set_descricao(self, descricao):
        if descricao == "":
            raise ValueError("A descrição não pode ser vazia")
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
        if id <= 0:
            raise ValueError("O id deve ser positivo")
        self.id = id

    def set_titulo(self, titulo):
        if titulo == "":
            raise ValueError("O título não pode ser vazio")
        self.titulo = titulo

    def set_artista(self, artista):
        if artista == "":
            raise ValueError("O artista não pode ser vazio")
        self.artista = artista

    def set_album(self, album):
        if album == "":
            raise ValueError("O álbum não pode ser vazio")
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
    def __init__(self, id, idPlaylist, idMusica, sequencia):
        self.set_id(id)
        self.set_idPlaylist(idPlaylist)
        self.set_idMusica(idMusica)
        self.set_sequencia(sequencia)

    def set_id(self, id):
        if id <= 0:
            raise ValueError("O id deve ser positivo")
        self.id = id

    def set_idPlaylist(self, idPlaylist):
        if idPlaylist <= 0:
            raise ValueError("O id da playlist deve ser positivo")
        self.idPlaylist = idPlaylist

    def set_idMusica(self, idMusica):
        if idMusica <= 0:
            raise ValueError("O id da música deve ser positivo")
        self.idMusica = idMusica

    def set_sequencia(self, sequencia):
        if sequencia <= 0:
            raise ValueError("A sequência deve ser positiva")
        self.sequencia = sequencia

    def get_id(self):
        return self.id

    def get_idPlaylist(self):
        return self.idPlaylist

    def get_idMusica(self):
        return self.idMusica

    def get_sequencia(self):
        return self.sequencia

    def __str__(self):
        return f"{self.id} - {self.idPlaylist} - {self.idMusica} - {self.sequencia}"


class UI:
    Playlists = []
    Musicas = []
    Itens = []

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

        x = PlayList(id, nome, descricao)

        cls.Playlists.append(x)

        print("Playlist inserida com sucesso")

    @classmethod
    def listar_playlist(cls):
        if len(cls.Playlists) == 0:
            print("Nenhuma playlist cadastrada")

        else:
            for x in cls.Playlists:
                print(x)

    @classmethod
    def atualizar_playlist(cls):
        UI.listar_playlist()

        id = int(input("Informe o id da playlist: "))

        x = UI.Playlist_listarID(id)

        if x != None:
            cls.Playlists.remove(x)

            nome = input("Informe o novo nome: ")
            descricao = input("Informe a nova descrição: ")

            novo = PlayList(id, nome, descricao)

            cls.Playlists.append(novo)

            print("Playlist atualizada")

        else:
            print("Playlist não encontrada")

    @classmethod
    def excluir_playlist(cls):
        UI.listar_playlist()

        id = int(input("Informe o id da playlist: "))

        x = UI.Playlist_listarID(id)

        if x != None:
            cls.Playlists.remove(x)

            print("Playlist removida")

        else:
            print("Playlist não encontrada")

    @classmethod
    def inserir_musica(cls):
        id = int(input("Informe o id da música: "))
        titulo = input("Informe o título: ")
        artista = input("Informe o artista: ")
        album = input("Informe o álbum: ")

        x = Musica(id, titulo, artista, album)

        cls.Musicas.append(x)

        print("Música inserida com sucesso")

    @classmethod
    def listar_musica(cls):
        if len(cls.Musicas) == 0:
            print("Nenhuma música cadastrada")

        else:
            for x in cls.Musicas:
                print(x)

    @classmethod
    def atualizar_musica(cls):
        UI.listar_musica()

        id = int(input("Informe o id da música: "))

        x = UI.Musica_listarID(id)

        if x != None:
            cls.Musicas.remove(x)

            titulo = input("Informe o novo título: ")
            artista = input("Informe o novo artista: ")
            album = input("Informe o novo álbum: ")

            novo = Musica(id, titulo, artista, album)

            cls.Musicas.append(novo)

            print("Música atualizada")

        else:
            print("Música não encontrada")

    @classmethod
    def excluir_musica(cls):
        UI.listar_musica()

        id = int(input("Informe o id da música: "))

        x = UI.Musica_listarID(id)

        if x != None:
            cls.Musicas.remove(x)

            print("Música removida")

        else:
            print("Música não encontrada")

    @classmethod
    def inserir_item(cls):
        id = int(input("Informe o id do item: "))
        idPlaylist = int(input("Informe o id da playlist: "))
        idMusica = int(input("Informe o id da música: "))
        sequencia = int(input("Informe a sequência: "))

        if UI.Playlist_listarID(idPlaylist) == None:
            print("Playlist não encontrada")
            return

        if UI.Musica_listarID(idMusica) == None:
            print("Música não encontrada")
            return

        x = PlayListItem(id, idPlaylist, idMusica, sequencia)

        cls.Itens.append(x)

        print("Item inserido com sucesso")

    @classmethod
    def listar_item(cls):
        if len(cls.Itens) == 0:
            print("Nenhum item cadastrado")

        else:
            for x in cls.Itens:
                print(x)

    @classmethod
    def atualizar_item(cls):
        UI.listar_item()

        id = int(input("Informe o id do item: "))

        x = UI.Item_listarID(id)

        if x != None:
            cls.Itens.remove(x)

            idPlaylist = int(input("Informe o novo id da playlist: "))
            idMusica = int(input("Informe o novo id da música: "))
            sequencia = int(input("Informe a nova sequência: "))

            novo = PlayListItem(id, idPlaylist, idMusica, sequencia)

            cls.Itens.append(novo)

            print("Item atualizado")

        else:
            print("Item não encontrado")

    @classmethod
    def excluir_item(cls):
        UI.listar_item()

        id = int(input("Informe o id do item: "))

        x = UI.Item_listarID(id)

        if x != None:
            cls.Itens.remove(x)

            print("Item removido")

        else:
            print("Item não encontrado")

    @classmethod
    def Playlist_listarID(cls, id):
        for x in cls.Playlists:
            if x.get_id() == id:
                return x

        return None

    @classmethod
    def Musica_listarID(cls, id):
        for x in cls.Musicas:
            if x.get_id() == id:
                return x

        return None

    @classmethod
    def Item_listarID(cls, id):
        for x in cls.Itens:
            if x.get_id() == id:
                return x

        return None


UI.main()