from exceptions.valor_invalido_exception import ValorInvalido
import os


class TelaDoacao():
    def tela_opcoes(self):
        print("Escolha uma opção:")
        print("[1] Cadastrar doacao.")
        print("[2] Alterar doacao.")
        print("[3] Excluir doacao.")
        print("[4] Listar doacoes.")
        print("[0] Retornar para o menu princiapal.")
        while True:
            try:
                opcao_escolhida = int(input("Opção: "))
                if 0 < opcao_escolhida > 4:
                    raise ValorInvalido
            except (ValorInvalido, ValueError):
                print("Valor inválido! Digite uma das opções.")
            else:
                break
        os.system('cls')
        return opcao_escolhida

    def pega_dados_doacao(self):
        data_doacao = input("Data de doação: ")
        codigo_animal = input("Código do animal: ")
        cpf_doador = input("Cpf do doador: ")
        motivo = input("Motivo da doação: ")

        return {"data_doacao": data_doacao, "codigo_animal": codigo_animal,
                "cpf_doador": cpf_doador, "motivo": motivo}

    def mostra_doacao(self, dados_doacao):
        print("Código da doação: ", dados_doacao["id"])
        print("Data da doação: ", dados_doacao["data_doacao"])
        print("Nome/Cpf do doador: ", f'{dados_doacao["nome_doador"]} / " \
              {dados_doacao["cpf_doador"]}')
        print("Nome/Código do animal: ", f'{dados_doacao["nome_animal"]} / " \
              {dados_doacao["codigo_animal"]}')
        print("Motivo da doação: ", dados_doacao["motivo"])
        print("\n")
        pass

    def seleciona_doacao(self):
        codigo = input("Código da doação que deseja selecionar: ")
        return codigo

    def mensagem(self, mensagem: str):
        print(mensagem)
