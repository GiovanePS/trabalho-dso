from exceptions.valor_invalido_exception import ValorInvalido
import os


class TelaVacinacao():
    def tela_opcoes(self):
        print("Escolha uma opção:")
        print("[1] Registrar vacinação.")
        print("[2] Alterar vacinação.")
        print("[3] Excluir vacinação.")
        print("[4] Listar vacinações.")
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

    def pega_dados_vacinacao(self):
        data_vacinacao = input("Data da vacinação: ")
        codigo_animal_vacinado = input("Código do animal vacinado: ")
        codigo_vacina = input("Código da vacina aplicada: ")
        return {"data_vacinacao": data_vacinacao,
                "codigo_animal_vacinado": codigo_animal_vacinado,
                "codigo_vacina": codigo_vacina}
    
    def mostra_mensagem(self, msg):
        print(msg)

    def mostra_vacinacao(self, dados_vacinacao):
        print("Codigo da vacinação: ", dados_vacinacao["codigo_vacinacao"])
        print("Data da vacinação: ", dados_vacinacao["data_vacinacao"])
        print("Nome/Código do animal vacinado: ", f'{dados_vacinacao["nome_animal"]} / {dados_vacinacao["codigo_animal"]}')
        print("Nome/Código da vacina: ", f'{dados_vacinacao["nome_vacina"]} / {dados_vacinacao["codigo_vacina"]}')
        print("\n")

    def seleciona_vacinacao(self):
        id_vacinacao = input("Código da vacinação que deseja selecionar: ")
        return id_vacinacao