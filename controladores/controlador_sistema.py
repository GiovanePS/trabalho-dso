from telas.tela_sistema import TelaSistema
from controladores.controlador_animal import ControladorAnimal
from time import sleep
import os


class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_animais = ControladorAnimal(self)

    def inicializa_sistema(self):
        print("Bem-vindo(a)!")
        sleep(1)
        self.abre_tela()

    def cadastra_animais(self):
        self.__controlador_animais.abre_tela()

    def encerra_sistema(self):
        print("Até logo!")
        sleep(1)
        exit()

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_animais, 0: self.encerra_sistema}

        while True:
            opcao = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()
            os.system('cls')
