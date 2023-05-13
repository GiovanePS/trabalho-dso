from entidades.adocao import Adocao
from exceptions.valor_invalido_exception import ValorInvalido
from datetime import date
import os

class TelaAdocao():
    def __init__(self):
        ...

    def tela_opcoes(self):
        print("Escolha uma opção:")
        print("[1] Cadastrar adocao.")
        print("[2] Alterar adocao.")
        print("[3] Excluir adocao.")
        print("[4] Listar adocoes.")
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
    
    def pega_dados_adocao(self):
        data_adocao=input("Data da adoção: ")
        codigo_animal_adotado=input("Código do animal adotado: ")
        cpf_adotante=input("Cpf do adotante: ")
        print("Assinar termo de responsabilidade: ")
        while True:
            print("  [1] Sim.")
            print("  [2] Não.")
            try:
                opcao_tipo = int(input("  Opção: "))
                if opcao_tipo != 1 and opcao_tipo != 2:
                    raise ValorInvalido
                elif opcao_tipo==1:
                    assinatura=True
                    break
                elif opcao_tipo==2:
                    assinatura=False
                    break
            except (ValorInvalido, ValueError):
                print("Valor inválido! Digite uma das opções.")
        return{"data_adocao":data_adocao, "codigo_animal_adotado":codigo_animal_adotado, "cpf_adotante":cpf_adotante, "assinatura":assinatura}
    
    def mostra_mensagem(self, msg):
        print(msg)
    
    def mostra_adocao(self, dados_adocao):
        print("Codigo da adoção: ", dados_adocao["codigo_adocao"])
        print("Data da adoção: ", dados_adocao["data_adocao"])
        print("Nome/Código do animal: ", f'{dados_adocao["nome_animal"]} / {dados_adocao["codigo_animal"]}')
        print("Nome/Cpf do adotante: ", f'{dados_adocao["nome_adotante"]} / {dados_adocao["cpf_adotante"]}')
        print("Termo de responsabilidade assinado: ", dados_adocao["assinatura"])
        print("\n")
    
    def seleciona_adocao(self):
        id_adocao= input("Código da adoção que deseja selecionar: ")
        return id_adocao