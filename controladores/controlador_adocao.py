from telas.tela_adocao import TelaAdocao
from entidades.adocao import Adocao
import os


class ControladorAdocao:
    def __init__(self):
        self.__adocoes = []
        self.__tela_adocao = TelaAdocao()
    
    def incluir_adocao(self):
        print('incluindo animal')

    def alterar_adocao(self):
        print('alterando animal')

    def excluir_adocao(self):
        print('excluindo animal')

    def listar_adocoes(self):
        print('listando animais')

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_adocao, 2: self.alterar_adocao,
                        3: self.excluir_adocao, 4: self.listar_adocoes,
                        0: "Retornar para menu principal"}
        while True:
            opcao = self.__tela_adocao.tela_opcoes()
            if opcao == 0:
                return
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()