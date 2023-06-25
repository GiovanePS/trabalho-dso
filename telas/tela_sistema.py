import PySimpleGUI as sg
from exceptions.valor_invalido_exception import ValorInvalido
import os


class TelaSistema:
    def __init__(self):
        self.__window = None
        sg.ChangeLookAndFeel("Light Gray")

    def abre_tela(self):
        self.tela_principal()
        button, values = self.open()
        if button is None or values["0"]:
            opcao_escolhida = 0
        elif values["1"]:
            opcao_escolhida = 1
        elif values["2"]:
            opcao_escolhida = 2
        elif values["3"]:
            opcao_escolhida = 3
        elif values["4"]:
            opcao_escolhida = 4
        elif values["5"]:
            opcao_escolhida = 5
        elif values["6"]:
            opcao_escolhida = 6
        elif values["7"]:
            opcao_escolhida = 7
        self.close()
        return opcao_escolhida

    def tela_principal(self):
        layout = [
            [sg.Radio("Animais.", "Radio1", key="1")],
            [sg.Radio("Doadores.", "Radio1", key="2")],
            [sg.Radio("Adotantes.", "Radio1", key="3")],
            [sg.Radio("Doações.", "Radio1", key="4")],
            [sg.Radio("Adoções.", "Radio1", key="5")],
            [sg.Radio("Vacinações.", "Radio1", key="6")],
            [sg.Radio("Menu de relatórios.", "Radio1", key="7")],
            [sg.Radio("Finalizar sistema.", "Radio1", default=True, key="0")],
            [sg.Push(), sg.Button("Confirmar")],
        ]
        self.__window = sg.Window("Menu principal", layout, finalize=True)
        self.__window.set_min_size((300, 200))

    def mensagem(self, mensagem: str):
        sg.Popup("", mensagem)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()
