from telas.tela_doacao import TelaDoacao
from entidades.doacao import Doacao
import os

class ControladorDoacao:
    def __init__(self):
        self.__doacoes = []
        self.__tela_doacao = TelaDoacao()
    
    def incluir_doacao(self):
        print('incluindo animal')

    def alterar_doacao(self):
        print('alterando animal')

    def excluir_doacao(self):
        print('excluindo animal')

    def listar_doacoes(self):
        print('listando animais')

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_doacao, 2: self.alterar_doacao,
                        3: self.excluir_doacao, 4: self.listar_doacoes,
                        0: "Retornar para menu principal"}
        while True:
            opcao = self.__tela_doacao.tela_opcoes()
            if opcao == 0:
                return
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()