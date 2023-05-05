class TelaSistema:
    def tela_opcoes(self):
        print("Escolha um dos Menus:")
        print("[1] Animais.")
        print("[2] Doadores")
        print("[0] Finalizar sistema.")
        try:
            opcao_escolhida = int(input("Opção: "))
        except ValueError:
            print("Digite uma das opções!")
        return opcao_escolhida
