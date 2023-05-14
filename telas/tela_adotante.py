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
                opcao_escolhida = int(input("Opção: "))
                if 0 < opcao_escolhida > 4:
                    raise ValorInvalido
            except (ValorInvalido, ValueError):
                print("Valor inválido! Digite uma das opções.")
            else:
                break
        os.system('cls')
        return opcao_escolhida

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
                        ano = int(input("Ano de nascimento do adotante: "))
                        if 1900 <= ano <= 2023:
                            break
                        else:
                            raise ValorInvalido
                    except (ValorInvalido, ValueError):
                        print("Digite um ano de nascimento válido!")

                while True:
                    try:
                        mes = int(input("Mês de nascimento do adotante: "))
                        if 1 <= mes <= 12:
                            break
                        else:
                            raise ValorInvalido
                    except (ValorInvalido, ValueError):
                        print("Digite um mês de nascimento válido!")

                while True:
                    try:
                        dia = int(input("Dia de nascimento do adotante: "))
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
            print("[1] Casa pequena.")
            print("[2] Casa média.")
            print("[3] Casa grande.")
            print("[4] Apartamento pequeno.")
            print("[5] Apartamento médio.")
            print("[6] Apartamento grande.")
            try:
                opcao_tipo_habitacao = int(input("Opção: "))
                if 1 < opcao_tipo_habitacao > 6:
                    raise ValorInvalido
            except (ValorInvalido, ValueError):
                print(
                    "Valor inválido! Digite um dos valores inteiros válidos.")
            else:
                break
        tipos_de_habitacoes = {
            1: "Casa pequena",
            2: "Casa média",
            3: "Casa grande",
            4: "Apartamento pequeno",
            5: "Apartamento médio",
            6: "Apartamento grande"
        }

        tipo_habitacao = tipos_de_habitacoes[opcao_tipo_habitacao]

        while True:
            print("Tem animais?")
            print("[1] Sim")
            print("[2] Não")
            try:
                tem_animais = int(input("Opção: "))
                if 1 < tem_animais > 2:
                    raise ValorInvalido
            except (ValorInvalido, ValueError):
                print("Valor inválido! Digite um valor inteiro válido.")
            else:
                break
        tem_animais = True if tem_animais == 1 else False

        return {"cpf": cpf,
                "nome": nome,
                "data_nascimento": data_nascimento,
                "endereco": endereco,
                "tipo_habitacao": tipo_habitacao,
                "tem_animais": tem_animais}

    def mostra_adotante(self, adotante: Adotante):
        print(f'{adotante.cpf} - {adotante.nome}, {adotante.data_nascimento}\n'
              f'\tEndereço: {adotante.endereco}')
        print()
        
    def seleciona_cpf(self):
        while True:
            cpf = input("Digite o CPF: ")
            if cpf_validador(cpf):
                return cpf
            else:
                print("CPF inválido. Digite novamente.")

    def mensagem(self, mensagem: str):
        print(mensagem)
