from exceptions.valor_invalido_exception import ValorInvalido
from entidades.adotante import Adotante
from utils.cpf_validador import cpf_validador
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

    def pega_dados_adotante(self):
        while True:
            cpf = input("CPF: ")
            if cpf_validador(cpf):
                break
            else:
                print("CPF inválido. Digite novamente.")

        nome = input("Nome: ")

        while True:
            try:
                while True:
                    try:
                        ano = int(input("Ano de nascimento do doador: "))
                        if 1900 <= ano <= 2023:
                            break
                        else:
                            raise ValorInvalido
                    except (ValorInvalido, ValueError):
                        print("Digite um ano de nascimento válido!")

                while True:
                    try:
                        mes = int(input("Mês de nascimento do doador: "))
                        if 1 <= mes <= 12:
                            break
                        else:
                            raise ValorInvalido
                    except (ValorInvalido, ValueError):
                        print("Digite um mês de nascimento válido!")

                while True:
                    try:
                        dia = int(input("Dia de nascimento do doador: "))
                        if 1 <= dia <= 31:
                            break
                        else:
                            raise ValorInvalido
                    except (ValorInvalido, ValueError):
                        print("Digite um dia de nascimento válido!")
                data_nascimento = date(ano, mes, dia)
            except ValueError:
                print("Data inválida. Digite a data novamente!")
            else:
                break

        endereco = input("Endereço: ")
        while True:
            print("Tipo de habitação: ")
            print("[1] Casa.")
            print("[2] Apartamento.")
            try:
                tipo_habitacao = int(input("Opção: "))
                if tipo_habitacao != 1 and tipo_habitacao != 2:
                    raise ValorInvalido
            except (ValorInvalido, ValueError):
                print("Valor inválido! Digite um valor inteiro válido.")
            else:
                break
        if tipo_habitacao == 1:
            tipo_habitacao = "Casa"
        else:
            tipo_habitacao = "Apartamento."

        while True:
            print("Tem animais?")
            print("[1] Sim")
            print("[2] Não")
            try:
                tem_animais = int(input("Opção: "))
                if tem_animais != 1 and tem_animais != 2:
                    raise ValorInvalido
            except (ValorInvalido, ValueError):
                print("Valor inválido! Digite um valor inteiro válido.")
            else:
                break
        if tem_animais == 1:
            tem_animais = "Sim"
        else:
            tem_animais = "Não"

        return {"cpf": cpf,
                "nome": nome,
                "data_nascimento": data_nascimento,
                "endereco": endereco,
                "tipo_habitacao": tipo_habitacao,
                "tem_animais": tem_animais}

    def mostra_adotante(self, adotante: Adotante):
        print(f'{adotante.cpf} - {adotante.nome}, {adotante.data_nascimento}\n'
              f'\tEndereço: {adotante.endereco}')

    def seleciona_cpf(self):
        while True:
            cpf = input("Digite o CPF: ")
            if cpf_validador(cpf):
                return cpf
            else:
                print("CPF inválido. Digite novamente.")

    def mensagem(self, mensagem: str):
        print(mensagem)
