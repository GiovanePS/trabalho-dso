from exceptions.valor_invalido_exception import ValorInvalido
import os


class TelaVacinacao():
    def tela_opcoes(self):
        print("Escolha uma opção:")
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
