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
        print(f'{adotante.cpf} - {adotante.nome}, {adotante.data_nascimento}\n'
              f'\tEndereço: {adotante.endereco}')

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
