from exceptions.valor_invalido_exception import ValorInvalido
from entidades.adotante import Adotante
from datetime import date
import os


class TelaAdotante:
    def abre_tela(self):
        print("Escolha uma opcão:")
        print("[1] Cadastrar adotante.")
        print("[2] Alterar adotante.")
        print("[3] Excluir adotante.")
        print("[4] Listar adotantes.")
        print("[0] Retornar para o menu principal.")
        while True:
            try:
                opcao = int(input("Opção: "))
                if 0 < opcao > 4:
                    raise ValorInvalido
            except (ValorInvalido, ValueError):
                print("Valor inválido! Digite uma das opções.")
            else:
                break
        os.system('cls')
        return opcao

    def pega_dados(self):
        cpf = input("CPF: ")
        nome = input("Nome: ")
        ano_nascimento = input("Ano de nascimento: ")
        mes_nascimento = input("Mês de nascimento: ")
        dia_nascimento = input("Dia de nascimento: ")
        data_nascimento = date(ano_nascimento, mes_nascimento, dia_nascimento)
        endereco = input("Endereço: ")
        tipo_habitacao = input("Tipo de habitação: ")
        print("Tem animais?")
        print("[1] Sim")
        print("[2] Não")
        tem_animais = input("Opção: ")

        return {"cpf": cpf,
                "nome": nome,
                "data_nascimento": data_nascimento,
                "endereco": endereco,
                "tipo_habitacao": tipo_habitacao,
                "tem_animais": tem_animais}

    def mostra_adotante(self, adotante: Adotante):
        print(f"{adotante}")

    def seleciona_cpf(self):
        while True:
            try:
                cpf = input("Digite o CPF: ")
            except ValueError:
                print("Valor inválido! Digite um valor inteiro válido.")
            else:
                break
        return cpf

    def mensagem(self, mensagem: str):
        print(mensagem)
