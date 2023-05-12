from telas.tela_doacao import TelaDoacao
from entidades.doacao import Doacao
import os
from controladores.controlador_animal import *


class ControladorDoacao():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema=controlador_sistema
        self.__doacoes = []
        self.__id=0
        self.__tela_doacao = TelaDoacao()

    def pega_doacao_por_codigo(self,codigo:int):
        for doacao in self.__doacoes:
            if doacao.codigo == codigo:
                return doacao
            
    def incluir_doacao(self):
        self.__controlador_sistema.controlador_animais.listar_animais()
        self.__controlador_sistema.controlador_doador.listar_doadores()

        dados_doacao = self.__tela_doacao.pega_dados_doacao()

        self.__id += 1
        self.__tela_doacao.mensagem("Cadastro de doação:")
        
        animal = self.__controlador_sistema.controlador_animais.pegar_animal_por_codigo(dados_doacao["codigo_animal"])
        doador = self.__controlador_sistema.controlador_doador.pega_doador_por_cpf(dados_doacao["cpf_doador"])

        # if (doador is not None and animal is not None):
        doacao = Doacao(dados_doacao["data_doacao"],
                        animal, doador,
                        dados_doacao["motivo"], self.__id)
        self.__doacoes.append(doacao)
        # else:
            # self.__tela_doacao.mensagem("Dados inválidos!")
        os.system('cls')
        self.__tela_doacao.mensagem("Doação cadastrada com sucesso.")
        print()

    def alterar_doacao(self):
        print('alterando animal')

    def excluir_doacao(self):
        print('excluindo animal')

    def listar_doacoes(self):
        if len(self.__doacoes)==0:
            print("Não há nenhuma doação cadastrada!")
        else:
            print("Doações:")
            for d in self.__doacoes:
                self.__tela_doacao.mostra_doacao({"nome_doador": d.doador.nome,
                                                  "cpf_doador": d.doador.cpf,
                                                  "nome_animal": d.animal.nome,
                                                  "codigo_animal": d.animal.codigo,
                                                  "motivo":d.motivo})

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