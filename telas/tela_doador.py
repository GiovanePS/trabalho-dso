from entidades.doador import Doador


class TelaDoador():
    def __init__(self):
        ...

    def tela_opcoes(self):
        print("Escolha uma opção:")
        print("[1] Cadastrar doador.")
        print("[2] Alterar doador.")
        print("[3] Excluir doador.")
        print("[4] Listar doadores.")
        print("[0] Retornar para o menu princiapal.")

    def pega_cpf(self):
        cpf = input("Digite o CPF do doador: ")
        return cpf

    def pega_dados_doador(self):
        cpf = input("CPF do doador: ")
        nome = input("Nome do doador: ")
        data_nascimento = input("Data de nascimento do doador: ")
        endereco = input("Endereço do doador: ")

        return {"cpf": cpf, "nome": nome,
                "data_nascimento": data_nascimento,
                "endereco": endereco}

    def mostra_doador(self, doador: Doador):
        print(f"{doador.cpf} - {doador.nome}, {doador.data_nascimento}\n\
              Endereço: \t{doador.endereco}")

    def mensagem(self, mensagem: str):
        print(mensagem)
