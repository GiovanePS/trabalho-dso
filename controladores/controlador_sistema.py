from telas.tela_sistema import TelaSistema
from controladores.controlador_animal import ControladorAnimal
from controladores.controlador_doador import ControladorDoador
from time import sleep
import os


class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_animais = ControladorAnimal()
        self.__controlador_doador = ControladorDoador()

    def inicializa_sistema(self):
        print("Bem-vindo(a)!")
        sleep(1)
        os.system('cls')
        self.abre_tela()

    def menu_animais(self):
        self.__controlador_animais.abre_tela()

    def menu_doador(self):
        self.__controlador_doador.abre_tela()

    def encerra_sistema(self):
        print("Até logo!")
        sleep(1)
        exit()

    def abre_tela(self):
        lista_opcoes = {1: self.menu_animais, 2: self.menu_doador,
                        0: self.encerra_sistema}

        while True:
            opcao = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao]
            os.system('cls')
            funcao_escolhida()
