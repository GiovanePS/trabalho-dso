class TelaSistema:
    def tela_opcoes(self):
        print("Escolha um dos Menus:")
        print("[1] Animais.")
        print("[0] Finalizar sistema.")
        try:
            opcao_escolhida = int(input("Opção: "))
        except TypeError:
            print("Digite uma das opções!")
        return opcao_escolhida
