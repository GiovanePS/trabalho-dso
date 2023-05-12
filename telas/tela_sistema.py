from exceptions.valor_invalido_exception import ValorInvalido
import os


class TelaSistema:
    def tela_opcoes(self):
        print("Escolha um dos Menus:")
        print("[1] Animais.")
        print("[2] Doadores")
        print("[3] Adotante")
        print("[4] Doações")
        print("[5] Adoções")
        print("[6] Vacinações")
        print("[0] Finalizar sistema.")
        while True:
            try:
                opcao_escolhida = int(input("Opção: "))
                if 0 < opcao_escolhida > 6:
                    raise ValorInvalido
            except (ValorInvalido, ValueError):
                print("Valor inválido! Digite uma das opções.")
            else:
                break
        os.system('cls')
        return opcao_escolhida
