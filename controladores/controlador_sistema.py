from telas.tela_sistema import TelaSistema
from controladores.controlador_animal import ControladorAnimal
from controladores.controlador_doador import ControladorDoador
from controladores.controlador_adotante import ControladorAdotante
from controladores.controlador_doacao import ControladorDoacao
from controladores.controlador_adocao import ControladorAdocao
from controladores.controlador_vacinacao import ControladorVacinacao
from controladores.controlador_vacina import ControladorVacina
from controladores.controlador_menu_relatorios import ControladorMenuRelatorios
from time import sleep
import os


class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_animal = ControladorAnimal(self)
        self.__controlador_doador = ControladorDoador(self)
        self.__controlador_adotante = ControladorAdotante(self)
        self.__controlador_doacao = ControladorDoacao(self)
        self.__controlador_adocao = ControladorAdocao(self)
        self.__controlador_vacinacao = ControladorVacinacao(self)
        self.__controlador_vacina = ControladorVacina(self)
        self.__controlador_menu_relatorios = ControladorMenuRelatorios(self)

    @property
    def controlador_animal(self):
        return self.__controlador_animal

    @property
    def controlador_doador(self):
        return self.__controlador_doador

    @property
    def controlador_adotante(self):
        return self.__controlador_adotante

    @property
    def controlador_vacina(self):
        return self.__controlador_vacina

    def inicializa_sistema(self):
        print("Bem-vindo(a)!")
        sleep(1)
        os.system("cls")
        self.abre_tela()

    def menu_animais(self):
        self.__controlador_animal.abre_tela()

    def menu_doador(self):
        self.__controlador_doador.abre_tela()

    def menu_adotante(self):
        self.__controlador_adotante.abre_tela()

    def menu_doacao(self):
        self.__controlador_doacao.abre_tela()

    def menu_adocao(self):
        self.__controlador_adocao.abre_tela()

    def menu_vacinacao(self):
        self.__controlador_vacinacao.abre_tela()

    def menu_vacina(self):
        self.__controlador_vacina.abre_tela()

    def menu_relatorios(self):
        self.__controlador_menu_relatorios.abre_tela()

    def encerra_sistema(self):
        print("Até logo!")
        sleep(1)
        exit()

    def abre_tela(self):
        lista_opcoes = {
            1: self.menu_animais,
            2: self.menu_doador,
            3: self.menu_adotante,
            4: self.menu_doacao,
            5: self.menu_adocao,
            6: self.menu_vacina,
            7: self.menu_vacinacao,
            8: self.menu_relatorios,
            0: self.encerra_sistema,
        }

        while True:
            opcao = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao]
            os.system("cls")
            funcao_escolhida()
