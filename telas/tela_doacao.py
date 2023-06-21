from exceptions.valor_invalido_exception import ValorInvalido
import os
from datetime import date
import PySimpleGUI as sg


class TelaDoacao:
    def __init__(self):
        self.__window = None
        sg.ChangeLookAndFeel('Light Gray')

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
                if 0 > opcao_escolhida or opcao_escolhida > 4:
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
                        if 1 > dia or dia > 31:
                            raise ValorInvalido
                        else:
                            break
                    except (ValorInvalido, ValueError):
                        print("Digite um dia válido!")
                while True:
                    try:
                        mes = int(input("Mês da doação: "))
                        if 1 > mes or mes > 12:
                            raise ValorInvalido
                        else:
                            break
                    except (ValorInvalido, ValueError):
                        print("Digite um mês válido!")

                while True:
                    try:
                        ano = int(input("Ano da doação: "))
                        if 1900 > ano or ano > 2023:
                            raise ValorInvalido
                        else:
                            break
                    except (ValorInvalido, ValueError):
                        print("Digite um ano válido!")

                data_doacao = date(ano, mes, dia)
            except ValueError:
                print("Data inválida. Digite a data novamente!")
            else:
                break
            
            self.controlador_sistema.controlador_animal.teste()

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

    def mostra_doacao(self, doacao):
        print("Código da doação:", doacao.id_doacao)
        print("Data da doação:", doacao.data_doacao)
        print(
            "Nome/CPF do doador:",
            f'{doacao.doador.nome} / {doacao.doador.cpf}',
        )
        print(
            "Nome/Código do animal:",
            f'{doacao.animal.nome} / {doacao.animal.codigo}',
        )
        print("Motivo da doação:", doacao.motivo)
        print("\n")
        pass

    def seleciona_doacao(self):
        codigo = input("Código da doação que deseja selecionar: ")
        return codigo

    def mensagem(self, mensagem: str):
        print(mensagem)
