from exceptions.valor_invalido_exception import ValorInvalido
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
                if 0 <= opcao <= 4:
                    raise ValorInvalido
            except (ValorInvalido, ValueError):
                print("Valor inválido! Digite uma das opções.")
            else:
                break
        os.system('cls')
        return opcao
