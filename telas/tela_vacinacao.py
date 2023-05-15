from exceptions.valor_invalido_exception import ValorInvalido
import os
from datetime import date


class TelaVacinacao:
    def tela_opcoes(self):
        print("Escolha uma opção:")
        print("[1] Registrar vacinação.")
        print("[2] Alterar vacinação.")
        print("[3] Excluir vacinação.")
        print("[4] Listar vacinações.")
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
        os.system('cls')
        return opcao_escolhida

    def pega_dados_vacinacao(self):
        while True:
            try:
                while True:
                    try:
                        dia = int(input("Dia da vacinação: "))
                        if 1 <= dia <= 31:
                            break
                        else:
                            raise ValorInvalido
                    except (ValorInvalido, ValueError):
                        print("Digite um dia válido!")
                while True:
                    try:
                        mes = int(input("Mês da vacinação: "))
                        if 1 <= mes <= 12:
                            break
                        else:
                            raise ValorInvalido
                    except (ValorInvalido, ValueError):
                        print("Digite um mês válido!")

                while True:
                    try:
                        ano = int(input("Ano da vacinação: "))
                        if 1900 <= ano <= 2023:
                            break
                        else:
                            raise ValorInvalido
                    except (ValorInvalido, ValueError):
                        print("Digite um ano válido!")

                data_vacinacao = date(ano, mes, dia)
            except ValueError:
                print("Data inválida. Digite a data novamente!")
            else:
                break
        while True:
            codigo = input("Código do animal vacinado: ")
            if codigo.isnumeric():
                codigo_animal_vacinado = codigo
                break
            else:
                print("ERRO. O código deve ser um número inteiro.")
        codigo_vacina = input("Código da vacina aplicada: ")
        return {"data_vacinacao": data_vacinacao,
                "codigo_animal_vacinado": codigo_animal_vacinado,
                "codigo_vacina": codigo_vacina}

    def mostra_mensagem(self, msg):
        print(msg)

    def mostra_vacinacao(self, dados_vacinacao):
        print("Codigo da vacinação: ", dados_vacinacao["codigo_vacinacao"])
        print("Data da vacinação: ", dados_vacinacao["data_vacinacao"])
        print("Nome/Código do animal vacinado: ", f'{dados_vacinacao["nome_animal"]} / {dados_vacinacao["codigo_animal"]}')
        print("Nome/Código da vacina: ", f'{dados_vacinacao["nome_vacina"]} / {dados_vacinacao["codigo_vacina"]}')
        print("\n")

    def seleciona_vacinacao(self):
        id_vacinacao = input("Código da vacinação que deseja selecionar: ")
        return id_vacinacao
