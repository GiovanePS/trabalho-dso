from exceptions.valor_invalido_exception import ValorInvalido
from datetime import date
import os


class TelaMenuRelatorios:
    def abre_tela(self):
        print("Menu de Relatórios:")
        print("[1] Animais disponíveis para adoção.")
        print("[2] Adoções de animais, filtradas por período.")
        print("[3] Doações de animais, filtradas por período.")
        print("[0] Retornar para o menu principal.")

        while True:
            try:
                opcao_escolhida = int(input("Opção: "))
                if 0 < opcao_escolhida > 3:
                    raise ValorInvalido
            except (ValorInvalido, ValueError):
                print("Valor inválido! Digite uma das opções.")
            else:
                break
        os.system("cls")
        return opcao_escolhida

    def pega_periodo(self):
        while True:
            try:
                while True:
                    try:
                        ano = int(input("Ano: "))
                        if 1900 <= ano <= 2023:
                            break
                        else:
                            raise ValorInvalido
                    except (ValorInvalido, ValueError):
                        print("Digite um ano válido!")

                while True:
                    try:
                        mes = int(input("Mês: "))
                        if 1 <= mes <= 12:
                            break
                        else:
                            raise ValorInvalido
                    except (ValorInvalido, ValueError):
                        print("Digite um mês válido!")

                while True:
                    try:
                        dia = int(input("Dia: "))
                        if 1 <= dia <= 31:
                            break
                        else:
                            raise ValorInvalido
                    except (ValorInvalido, ValueError):
                        print("Digite um dia válido!")
                periodo = date(ano, mes, dia)
            except ValueError:
                print("Data inválida. Digite a data novamente!")
            else:
                break

        return periodo

    def mensagem(self, mensagem):
        print(mensagem)
