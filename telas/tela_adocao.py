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
        print("[0] Retornar para o menu princiapal.")
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