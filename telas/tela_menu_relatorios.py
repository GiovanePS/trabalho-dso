from exceptions.valor_invalido_exception import ValorInvalido
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

    def mensagem(self, mensagem):
        print(mensagem)
