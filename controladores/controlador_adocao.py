from telas.tela_adocao import TelaAdocao
from entidades.adocao import Adocao
import os


class ControladorAdocao:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema=controlador_sistema
        self.__adocoes = []
        self.__tela_adocao = TelaAdocao()
        self.__id=0
    
    def incluir_adocao(self):
        self.__controlador_sistema.controlador_adotante.listar_adotantes()
        self.__controlador_sistema.controlador_animal.listar_animais()
        dados_adocao=self.__tela_adocao.pega_dados_adocao()


        adotante = self.__controlador_sistema.controlador_adotante.pega_adotante_por_cpf(dados_adocao["cpf_adotante"])
        animal = self.__controlador_sistema.controlador_animal.pegar_animal_por_codigo(dados_adocao["codigo_animal_adotado"])

        if (adotante is not None and animal is not None):
            self.__id+=1
            adocao=Adocao(dados_adocao["data_adocao", animal, adotante, dados_adocao["assinatura"], self.__id ])
            self.__adocoes.append(adocao)

        print(f'adotante: ', adotante)
        print(f'animal: ', animal) 
        print(f'adocao: ', adocao)
        
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