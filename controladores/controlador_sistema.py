from telas.tela_sistema import TelaSistema
from controladores.controlador_animal import ControladorAnimal
from controladores.controlador_doador import ControladorDoador
from controladores.controlador_adotante import ControladorAdotante
from controladores.controlador_doacao import ControladorDoacao
from time import sleep
import os


class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_animais = ControladorAnimal()
        self.__controlador_doador = ControladorDoador()
        self.__controlador_adotante = ControladorAdotante()
        self.__controlador_doacao = ControladorDoacao()

    def inicializa_sistema(self):
        print("Bem-vindo(a)!")
        sleep(1)
        os.system('cls')
        self.abre_tela()

    def menu_animais(self):
        self.__controlador_animais.abre_tela()

    def menu_doador(self):
        self.__controlador_doador.abre_tela()

    def menu_adotante(self):
        self.__controlador_adotante.abre_tela()

    def menu_doacao(self):
        self.__controlador_doacao.abre_tela()

    def encerra_sistema(self):
        print("Até logo!")
        sleep(1)
        exit()

    def abre_tela(self):
        lista_opcoes = {1: self.menu_animais, 2: self.menu_doador,
                        3: self.menu_adotante, 4: self.menu_doacao, 0: self.encerra_sistema}

        while True:
            opcao = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao]
            os.system('cls')
            funcao_escolhida()
