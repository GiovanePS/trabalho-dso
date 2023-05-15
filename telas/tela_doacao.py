from exceptions.valor_invalido_exception import ValorInvalido
import os
from datetime import date


class TelaDoacao:
    def tela_opcoes(self):
        print("Escolha uma opção:")
        print("[1] Registrar doação.")
        print("[2] Alterar doação.")
        print("[3] Excluir doação.")
        print("[4] Listar doações.")
        print("[0] Retornar para o menu principal.")
        while True:
            try:
                opcao_escolhida = int(input("Opção: "))
                if 0 < opcao_escolhida > 4:
                    raise ValorInvalido
            except (ValorInvalido, ValueError):
                print("Valor inválido! Digite uma das opções.")
            else:
                break
        os.system("cls")
        return opcao_escolhida

    def pega_dados_doacao(self):
        while True:
            try:
                while True:
                    try:
                        dia = int(input("Dia da doação: "))
                        if 1 <= dia <= 31:
                            break
                        else:
                            raise ValorInvalido
                    except (ValorInvalido, ValueError):
                        print("Digite um dia válido!")
                while True:
                    try:
                        mes = int(input("Mês da doação: "))
                        if 1 <= mes <= 12:
                            break
                        else:
                            raise ValorInvalido
                    except (ValorInvalido, ValueError):
                        print("Digite um mês válido!")

                while True:
                    try:
                        ano = int(input("Ano da doação: "))
                        if 1900 <= ano <= 2023:
                            break
                        else:
                            raise ValorInvalido
                    except (ValorInvalido, ValueError):
                        print("Digite um ano válido!")

                data_doacao = date(ano, mes, dia)
            except ValueError:
                print("Data inválida. Digite a data novamente!")
            else:
                break

        while True:
            codigo = input("Código do animal: ")
            if codigo.isnumeric():
                codigo_animal = codigo
                break
            else:
                print("ERRO. O código deve ser um número inteiro.")

        nome_animal = input("Nome do animal: ")
        cpf_doador = input("CPF do doador: ")
        nome_doador = input("Nome do doador: ")
        motivo = input("Motivo da doação: ")

        return {
            "data_doacao": data_doacao,
            "codigo_animal": codigo_animal,
            "nome_animal": nome_animal,
            "cpf_doador": cpf_doador,
            "nome_doador": nome_doador,
            "motivo": motivo,
        }

    def mostra_doacao(self, dados_doacao):
        print("Código da doação: ", dados_doacao["id"])
        print("Data da doação: ", dados_doacao["data_doacao"])
        print(
            "Nome/CPF do doador: ",
            f'{dados_doacao["nome_doador"]} / {dados_doacao["cpf_doador"]}',
        )
        print(
            "Nome/Código do animal: ",
            f'{dados_doacao["nome_animal"]} / {dados_doacao["codigo_animal"]}',
        )
        print("Motivo da doação: ", dados_doacao["motivo"])
        print("\n")
        pass

    def seleciona_doacao(self):
        codigo = input("Código da doação que deseja selecionar: ")
        return codigo

    def mensagem(self, mensagem: str):
        print(mensagem)
