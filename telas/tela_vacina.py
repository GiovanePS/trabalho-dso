from exceptions.valor_invalido_exception import ValorInvalido
from entidades.vacina import Vacina
import os
from random import randint


class TelaVacina:
    def abre_tela(self):
        print("Escolha uma opcão:")
        print("[1] Cadastrar vacina.")
        print("[2] Alterar vacina.")
        print("[3] Excluir vacina.")
        print("[4] Listar vacinas.")
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

    def pega_dados_vacina(self):
        while True:
            print("Nome da Vacina:")
            print("[1] Raiva")
            print("[2] Leptospirose")
            print("[3] Hepatite Infecciosa")
            print("[4] Outra")
            try:
                opcao = int(input("Opção: "))
                if 1 < opcao > 4:
                    raise ValorInvalido
            except (ValorInvalido, ValueError):
                print("Valor inválido! Digite um valor inteiro válido.")
            else:
                break
        tipos_de_vacina = {
            1: "Raiva",
            2: "Leptospirose",
            3: "Hepatite Infecciosa",
            4: "Outra",
        }
        if opcao == 4:
            nome_vacina = input("Outra: ")
        else:
            nome_vacina = tipos_de_vacina[opcao]

        while True:
            codigo = input("Código: ")
            if codigo.isnumeric():
                codigo_vacina = codigo
                break
            else:
                print("ERRO. O código deve ser um número inteiro.")

        return {"nome_vacina": nome_vacina, "codigo_vacina": codigo_vacina}

    def mostra_vacina(self, vacina: Vacina):
        print(f"{vacina.codigo_vacina} - {vacina.nome_vacina}")

    def seleciona_codigo(self):
        codigo = input("Digite o codigo: ")
        return codigo

    def mensagem(self, mensagem: str):
        print(mensagem)
