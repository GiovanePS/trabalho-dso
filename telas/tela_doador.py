from entidades.doador import Doador
from exceptions.valor_invalido_exception import ValorInvalido
from datetime import date
import os


class TelaDoador():
    def __init__(self):
        ...

    def tela_opcoes(self):
        print("Escolha uma opção:")
        print("[1] Cadastrar doador.")
        print("[2] Alterar doador.")
        print("[3] Excluir doador.")
        print("[4] Listar doadores.")
        print("[0] Retornar para o menu princiapal.")
        opcao_escolhida = int(input("Opção: "))
        os.system('cls')
        return opcao_escolhida

    def pega_cpf(self):
        cpf = input("Digite o CPF do doador: ")
        return cpf

    def pega_dados_doador(self):
        cpf = input("CPF do doador: ")
        nome = input("Nome do doador: ")

        while True:
            try:
                while True:
                    try:
                        ano = int(input("Ano de nascimento do doador: "))
                        if 1900 <= ano <= 2023:
                            break
                        else:
                            raise ValorInvalido
                    except (ValorInvalido, ValueError):
                        print("Digite um ano de nascimento válido!")

                while True:
                    try:
                        mes = int(input("Mês de nascimento do doador: "))
                        if 1 <= mes <= 12:
                            break
                        else:
                            raise ValorInvalido
                    except (ValorInvalido, ValueError):
                        print("Digite um mês de nascimento válido!")

                while True:
                    try:
                        dia = int(input("Dia de nascimento do doador: "))
                        if 1 <= dia <= 31:
                            break
                        else:
                            raise ValorInvalido
                    except (ValorInvalido, ValueError):
                        print("Digite um dia de nascimento válido!")
                data_nascimento = date(ano, mes, dia)
            except ValueError:
                print("Data inválida. Digite a data novamente!")
            else:
                break

        endereco = input("Endereço do doador: ")

        return {"cpf": cpf, "nome": nome,
                "data_nascimento": data_nascimento,
                "endereco": endereco}

    def mostra_doador(self, doador: Doador):
        print(f'{doador.cpf} - {doador.nome}, {doador.data_nascimento}\n'
              f'\tEndereço: {doador.endereco}')

    def mensagem(self, mensagem: str):
        print(mensagem)
