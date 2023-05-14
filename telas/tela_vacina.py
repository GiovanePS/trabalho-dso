from exceptions.valor_invalido_exception import ValorInvalido
from entidades.vacina import Vacina
import os


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
        os.system('cls')
        return opcao_escolhida

    def pega_dados_vacina(self):
        nome_vacina = input("Nome: ")
        while True:
            codigo = input("Código: ")
            if codigo.isnumeric():
                codigo_vacina=codigo
                break
            else:
                print("ERRO. O código deve ser um número inteiro.")

        return {"nome_vacina": nome_vacina, "codigo_vacina": codigo_vacina}

    def mostra_vacina(self, vacina: Vacina):
        print(f'Código: {vacina.codigo_vacina}')
        print(f'Vacina: {vacina.nome_vacina}')

    def seleciona_codigo(self):
        codigo = input("Digite o codigo: ")
        return codigo


    def mensagem(self, mensagem: str):
        print(mensagem)
