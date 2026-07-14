from service import Service

class UI:
    @staticmethod
    def main():
        op = 0
        while op != 15:
            try:
                op = UI.menu()
                if op == 1: UI.cliente_inserir()
                elif op == 2: UI.cliente_listar()
                elif op == 3: UI.cliente_atualizar()
                elif op == 4: UI.cliente_excluir()
                elif op == 5: UI.servico_inserir()
                elif op == 6: UI.servico_listar()
                elif op == 7: UI.servico_atualizar()
                elif op == 8: UI.servico_excluir()
                elif op == 9: UI.profissional_inserir()
                elif op == 10: UI.profissional_listar()
                elif op == 11: UI.profissional_pesquisar_id()
                elif op == 12: UI.profissional_pesquisar_nome()
                elif op == 13: UI.profissional_atualizar()
                elif op == 14: UI.profissional_excluir()
            except ValueError as e:
                print(f"Erro de validação: {e}")
            except Exception as e:
                print(f"Erro no sistema: {e}")

    @staticmethod
    def menu():
        print("\n" + "="*25 + " SISTEMA DE AGENDAMENTO " + "="*25)
        print("--- CAMADA DE CLIENTES ---")
        print("1-Inserir Cliente       2-Listar Clientes       3-Atualizar Cliente       4-Excluir Cliente")
        print("--- CAMADA DE SERVIÇOS ---")
        print("5-Inserir Serviço       6-Listar Serviços       7-Atualizar Serviço       8-Excluir Serviço")
        print("--- CAMADA DE PROFISSIONAIS ---")
        print("9-Inserir Profissional                          10-Listar Profissionais")
        print("11-Pesquisar Profissional por ID                12-Pesquisar Profissional por Nome")
        print("13-Atualizar Profissional                       14-Excluir Profissional")
        print("-" * 74)
        print("15-Sair")
        print("="*74)
        return int(input("Informe uma opção: "))

    @staticmethod
    def cliente_inserir():
        id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o telefone: ")
        senha = input("Informe a senha de acesso: ")
        Service.cliente_inserir(id, nome, email, fone, senha)

    @staticmethod
    def cliente_listar():
        print("\n--- Lista de Clientes ---")
        for obj in Service.cliente_listar(): print(obj)

    @staticmethod
    def cliente_atualizar():
        for obj in Service.cliente_listar(): print(obj)
        id = int(input("Informe o id do cliente a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        fone = input("Informe o novo telefone: ")
        senha = input("Informe a nova senha de acesso: ")
        Service.cliente_atualizar(id, nome, email, fone, senha)

    @staticmethod
    def cliente_excluir():
        for obj in Service.cliente_listar(): print(obj)
        id = int(input("Informe o id do cliente a ser excluído: "))
        Service.cliente_excluir(id)

    @staticmethod
    def servico_inserir():
        id = int(input("Informe o id do serviço: "))
        descricao = input("Informe a descrição: ")
        valor = float(input("Informe o valor (R$): "))
        Service.servico_inserir(id, descricao, valor)

    @staticmethod
    def servico_listar():
        print("\n--- Lista de Serviços ---")
        for obj in Service.servico_listar(): print(obj)

    @staticmethod
    def servico_atualizar():
        for obj in Service.servico_listar(): print(obj)
        id = int(input("Informe o id do serviço a ser atualizado: "))
        descricao = input("Informe a nova descrição: ")
        valor = float(input("Informe o novo valor (R$): "))
        Service.servico_atualizar(id, descricao, valor)

    @staticmethod
    def servico_excluir():
        for obj in Service.servico_listar(): print(obj)
        id = int(input("Informe o id do serviço a ser excluído: "))
        Service.servico_excluir(id)

    @staticmethod
    def profissional_inserir():
        id = int(input("Informe o id do profissional: "))
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        senha = input("Informe a senha: ")
        especialidade = input("Informe a especialidade: ")
        Service.profissional_inserir(id, nome, email, senha, especialidade)

    @staticmethod
    def profissional_listar():
        print("\n--- Lista de Profissionais ---")
        for obj in Service.profissional_listar(): print(obj)

    @staticmethod
    def profissional_pesquisar_id():
        id = int(input("Informe o ID do profissional que deseja buscar: "))
        obj = Service.profesional_listar_id(id)
        if obj:
            print("\nProfissional encontrado:")
            print(obj)
        else:
            print("\nProfissional não encontrado.")

    @staticmethod
    def profissional_pesquisar_nome():
        nome = input("Informe o nome (ou parte do nome) do profissional: ")
        resultados = Service.profissional_pesquisar_nome(nome)
        if resultados:
            print(f"\n--- Resultados da busca por '{nome}' ---")
            for obj in resultados: print(obj)
        else:
            print("\nNenhum profissional cadastrado corresponde a esse nome.")

    @staticmethod
    def profissional_atualizar():
        for obj in Service.profissional_listar(): print(obj)
        id = int(input("Informe o id do profissional a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        senha = input("Informe a nova senha: ")
        especialidade = input("Informe a nova especialidade: ")
        Service.profissional_atualizar(id, nome, email, senha, especialidade)

    @staticmethod
    def profissional_excluir():
        for obj in Service.profissional_listar(): print(obj)
        id = int(input("Informe o id do profissional a ser excluído: "))
        Service.profissional_excluir(id)

if __name__ == "__main__":
    UI.main()