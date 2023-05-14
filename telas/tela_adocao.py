from exceptions.valor_invalido_exception import ValorInvalido
import os


class TelaAdocao():
    def tela_opcoes(self):
        print("Escolha uma opção:")
        print("[1] Registrar adocao.")
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
        while True:
            data = input("Data da adoção (dia/mês/ano): ")
            if (1<=int(data[0:2])<=31) and (1<=int(data[3:5])<=12) and (1900<=int(data[6:10])<=2023):
                data_adocao = data
                break
            else:
                print("ERRO. Uma data válida deve ser preenchida conforme formato solicitado.")
        
        while True:
            codigo = input("Código do animal adotado: ")
            if codigo.isnumeric():
                codigo_animal_adotado=codigo
                break
            else:
                print("ERRO. O código deve ser um número inteiro.")
        nome_animal_adotado = input("Nome do animal adotado: ")
        cpf_adotante = input("Cpf do adotante: ")
        nome_adotante = input("Nome do adotante: ")
        print("Assinar termo de responsabilidade: ")
        while True:
            print("  [1] Sim.")
            print("  [2] Não.")
            try:
                opcao_tipo = int(input("  Opção: "))
                if opcao_tipo != 1 and opcao_tipo != 2:
                    raise ValorInvalido
                elif opcao_tipo == 1:
                    assinatura = True
                    break
                elif opcao_tipo == 2:
                    assinatura = False
                    break
            except (ValorInvalido, ValueError):
                print("Valor inválido! Digite uma das opções.")
        return {"data_adocao": data_adocao,
                "codigo_animal_adotado": codigo_animal_adotado,
                "nome_animal_adotado": nome_animal_adotado,
                "cpf_adotante": cpf_adotante,
                "nome_adotante": nome_adotante,
                "assinatura": assinatura}

    def mostra_mensagem(self, msg):
        print(msg)

    def mostra_adocao(self, dados_adocao):
        print("Codigo da adoção: ", dados_adocao["codigo_adocao"])
        print("Data da adoção: ", dados_adocao["data_adocao"])
        print("Nome/Código do animal: ", f'{dados_adocao["nome_animal"]} / {dados_adocao["codigo_animal"]}')
        print("Nome/Cpf do adotante: ", f'{dados_adocao["nome_adotante"]} / {dados_adocao["cpf_adotante"]}')
        print("Termo de responsabilidade assinado: ",
              dados_adocao["assinatura"])
        print("\n")

    def seleciona_adocao(self):
        id_adocao = input("Código da adoção que deseja selecionar: ")
        return id_adocao
