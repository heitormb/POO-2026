from service import Service

class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.cliente_inserir()
            elif op == 2: UI.cliente_listar()
            elif op == 3: UI.cliente_atualizar()
            elif op == 4: UI.cliente_excluir()
            elif op == 5: UI.servico_inserir()
            elif op == 6: UI.servico_listar()
            elif op == 7: UI.servico_atualizar()
            elif op == 8: UI.servico_excluir()

    @staticmethod
    def menu():
        print("\n" + "="*20 + " SISTEMA DE AGENDAMENTO " + "="*20)
        print("1-Inserir Cliente   2-Listar Clientes   3-Atualizar Cliente   4-Excluir Cliente")
        print("5-Inserir Serviço   6-Listar Serviços   7-Atualizar Serviço   8-Excluir Serviço")
        print("9-Sair")
        print("="*64)
        return int(input("Informe uma opção: "))

    @staticmethod
    def cliente_inserir():
        id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o telefone: ")
        Service.cliente_inserir(id, nome, email, fone)

    @staticmethod
    def cliente_listar():
        print("\n--- Clientes Cadastrados ---")
        for obj in Service.cliente_listar(): print(obj)

    @staticmethod
    def cliente_atualizar():
        for obj in Service.cliente_listar(): print(obj)
        id = int(input("Informe o id do cliente a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        fone = input("Informe o novo telefone: ")
        Service.cliente_atualizar(id, nome, email, fone)

    @staticmethod
    def cliente_excluir():
        for obj in Service.cliente_listar(): print(obj)
        id = int(input("Informe o id do cliente a ser excluído: "))
        Service.cliente_excluir(id)

    @staticmethod
    def servico_inserir():
        id = int(input("Informe o id do serviço: "))
        descricao = input("Informe a descrição do serviço: ")
        valor = float(input("Informe o valor do serviço (R$): "))
        Service.servico_inserir(id, descricao, valor)

    @staticmethod
    def servico_listar():
        print("\n--- Serviços Disponíveis ---")
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

if __name__ == "__main__":
    UI.main()