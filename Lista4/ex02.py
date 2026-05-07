class PlayList:
    def __init__(self, i: int, n: str, d: str):
        self.__id = i
        self.__nome = n
        self.__descricao = d

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_descricao(self):
        return self.__descricao

    def set_nome(self, nome):
        self.__nome = nome

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def ToString(self):
        return (
            f"ID: {self.__id} | "
            f"Nome: {self.__nome} | "
            f"Descrição: {self.__descricao}"
        )


class Musica:
    def __init__(self, i: int, t: str, art: str, alb: str):
        self.__id = i
        self.__titulo = t
        self.__artista = art
        self.__album = alb

    def get_id(self):
        return self.__id

    def get_titulo(self):
        return self.__titulo

    def get_artista(self):
        return self.__artista

    def get_album(self):
        return self.__album

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_artista(self, artista):
        self.__artista = artista

    def set_album(self, album):
        self.__album = album

    def ToString(self):
        return (
            f"ID: {self.__id} | "
            f"Título: {self.__titulo} | "
            f"Artista: {self.__artista} | "
            f"Álbum: {self.__album}"
        )


class PlayListItem:
    def __init__(self, i: int, ip: int, im: int, s: int):
        self.__id = i
        self.__idPlayList = ip
        self.__idMusica = im
        self.__sequencia = s

    def get_id(self):
        return self.__id

    def get_idPlayList(self):
        return self.__idPlayList

    def get_idMusica(self):
        return self.__idMusica

    def get_sequencia(self):
        return self.__sequencia

    def set_idPlayList(self, idplaylist):
        self.__idPlayList = idplaylist

    def set_idMusica(self, idmusica):
        self.__idMusica = idmusica

    def set_sequencia(self, sequencia):
        self.__sequencia = sequencia

    def ToString(self):
        return (
            f"ID Item: {self.__id} | "
            f"Playlist ID: {self.__idPlayList} | "
            f"Música ID: {self.__idMusica} | "
            f"Sequência: {self.__sequencia}"
        )


class UI:

    playlists = []
    musicas = []
    itens = []


    @staticmethod
    def inserir_playlist():
        print("\n=== INSERIR PLAYLIST ===")

        id_playlist = int(input("ID da playlist: "))
        nome = input("Nome da playlist: ")
        descricao = input("Descrição: ")

        playlist = PlayList(id_playlist, nome, descricao)
        UI.playlists.append(playlist)

        print("Playlist cadastrada com sucesso!")

    @staticmethod
    def listar_playlists():
        print("\n=== LISTA DE PLAYLISTS ===")

        if len(UI.playlists) == 0:
            print("Nenhuma playlist cadastrada.")
            return

        for p in UI.playlists:
            print(p.ToString())

    @staticmethod
    def atualizar_playlist():
        print("\n=== ATUALIZAR PLAYLIST ===")

        id_playlist = int(input("Informe o ID da playlist: "))

        for p in UI.playlists:
            if p.get_id() == id_playlist:

                novo_nome = input("Novo nome: ")
                nova_descricao = input("Nova descrição: ")

                p.set_nome(novo_nome)
                p.set_descricao(nova_descricao)

                print("Playlist atualizada!")
                return

        print("Playlist não encontrada.")

    @staticmethod
    def excluir_playlist():
        print("\n=== EXCLUIR PLAYLIST ===")

        id_playlist = int(input("Informe o ID da playlist: "))

        for p in UI.playlists:
            if p.get_id() == id_playlist:

                UI.itens = [
                    i for i in UI.itens
                    if i.get_idPlayList() != id_playlist
                ]

                UI.playlists.remove(p)

                print("Playlist removida!")
                return

        print("Playlist não encontrada.")

    @staticmethod
    def inserir_musica():
        print("\n=== INSERIR MÚSICA ===")

        id_musica = int(input("ID da música: "))
        titulo = input("Título: ")
        artista = input("Artista: ")
        album = input("Álbum: ")

        musica = Musica(id_musica, titulo, artista, album)
        UI.musicas.append(musica)

        print("Música cadastrada!")

    @staticmethod
    def listar_musicas():
        print("\n=== LISTA DE MÚSICAS ===")

        if len(UI.musicas) == 0:
            print("Nenhuma música cadastrada.")
            return

        for m in UI.musicas:
            print(m.ToString())

    @staticmethod
    def atualizar_musica():
        print("\n=== ATUALIZAR MÚSICA ===")

        id_musica = int(input("Informe o ID da música: "))

        for m in UI.musicas:
            if m.get_id() == id_musica:

                novo_titulo = input("Novo título: ")
                novo_artista = input("Novo artista: ")
                novo_album = input("Novo álbum: ")

                m.set_titulo(novo_titulo)
                m.set_artista(novo_artista)
                m.set_album(novo_album)

                print("Música atualizada!")
                return

        print("Música não encontrada.")

    @staticmethod
    def excluir_musica():
        print("\n=== EXCLUIR MÚSICA ===")

        id_musica = int(input("Informe o ID da música: "))

        for m in UI.musicas:
            if m.get_id() == id_musica:

                UI.itens = [
                    i for i in UI.itens
                    if i.get_idMusica() != id_musica
                ]

                UI.musicas.remove(m)

                print("Música removida!")
                return

        print("Música não encontrada.")


    @staticmethod
    def inserir_item():
        print("\n=== INSERIR ITEM NA PLAYLIST ===")

        id_item = int(input("ID do item: "))
        id_playlist = int(input("ID da playlist: "))
        id_musica = int(input("ID da música: "))
        sequencia = int(input("Sequência: "))

        playlist_existe = False
        for p in UI.playlists:
            if p.get_id() == id_playlist:
                playlist_existe = True
                break

        if not playlist_existe:
            print("Playlist não encontrada.")
            return

        musica_existe = False
        for m in UI.musicas:
            if m.get_id() == id_musica:
                musica_existe = True
                break

        if not musica_existe:
            print("Música não encontrada.")
            return

        item = PlayListItem(
            id_item,
            id_playlist,
            id_musica,
            sequencia
        )

        UI.itens.append(item)

        print("Item inserido na playlist!")

    @staticmethod
    def listar_itens():
        print("\n=== ITENS DAS PLAYLISTS ===")

        if len(UI.itens) == 0:
            print("Nenhum item cadastrado.")
            return

        for i in UI.itens:
            print(i.ToString())

    @staticmethod
    def listar_musicas_playlist():
        print("\n=== MÚSICAS DA PLAYLIST ===")

        id_playlist = int(input("Informe o ID da playlist: "))

        encontrou = False

        itens_ordenados = sorted(
            UI.itens,
            key=lambda x: x.get_sequencia()
        )

        for item in itens_ordenados:

            if item.get_idPlayList() == id_playlist:

                for musica in UI.musicas:

                    if musica.get_id() == item.get_idMusica():

                        print(
                            f"Sequência: {item.get_sequencia()}"
                        )
                        print(musica.ToString())
                        print("---------------------")

                        encontrou = True

        if not encontrou:
            print("Nenhuma música encontrada nessa playlist.")

    @staticmethod
    def excluir_item():
        print("\n=== EXCLUIR ITEM ===")

        id_item = int(input("Informe o ID do item: "))

        for i in UI.itens:
            if i.get_id() == id_item:

                UI.itens.remove(i)

                print("Item removido!")
                return

        print("Item não encontrado.")


    @staticmethod
    def menu():
        print("\n========== MENU ==========")
        print("1 - Inserir playlist")
        print("2 - Listar playlists")
        print("3 - Atualizar playlist")
        print("4 - Excluir playlist")
        print("5 - Inserir música")
        print("6 - Listar músicas")
        print("7 - Atualizar música")
        print("8 - Excluir música")
        print("9 - Inserir item na playlist")
        print("10 - Listar itens")
        print("11 - Listar músicas da playlist")
        print("12 - Excluir item")
        print("0 - Sair")

        return int(input("Escolha uma opção: "))

    @staticmethod
    def main():

        op = 1

        while op != 0:

            op = UI.menu()

            if op == 1:
                UI.inserir_playlist()

            elif op == 2:
                UI.listar_playlists()

            elif op == 3:
                UI.atualizar_playlist()

            elif op == 4:
                UI.excluir_playlist()

            elif op == 5:
                UI.inserir_musica()

            elif op == 6:
                UI.listar_musicas()

            elif op == 7:
                UI.atualizar_musica()

            elif op == 8:
                UI.excluir_musica()

            elif op == 9:
                UI.inserir_item()

            elif op == 10:
                UI.listar_itens()

            elif op == 11:
                UI.listar_musicas_playlist()

            elif op == 12:
                UI.excluir_item()

            elif op == 0:
                print("Programa encerrado!")

            else:
                print("Opção inválida!")


UI.main()