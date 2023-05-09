from telas.tela_vacinacao import TelaVacinacao
from entidades.vacinacao import Vacinacao
import os


class ControladorVacinacao:
    def __init__(self):
        self.__vacinacoes = []
        self.__tela_vacinacao = TelaVacinacao()
    
    def incluir_vacinacao(self):
        print('incluindo vacinas')

    def alterar_vacinacao(self):
        print('alterando vacinas')

    def excluir_vacinacao(self):
        print('excluindo vacinas')

    def listar_vacinacoes(self):
        print('listando vacinas')

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_vacinacao, 2: self.alterar_vacinacao,
                        3: self.excluir_vacinacao, 4: self.listar_vacinacoes,
                        0: "Retornar para menu principal"}
        while True:
            opcao = self.__tela_vacinacao.tela_opcoes()
            if opcao == 0:
                return
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()