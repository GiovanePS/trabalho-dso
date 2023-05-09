from entidades.doacao import Doacao
from exceptions.valor_invalido_exception import ValorInvalido
from datetime import date
import os

def TelaDoacao():
    def __init__(self):
        ...
    def tela_opcoes(self):
        print("Escolha uma opção:")
        print("[1] Cadastrar doacao.")
        print("[2] Alterar doacao.")
        print("[3] Excluir doacao.")
        print("[4] Listar doacoes.")
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