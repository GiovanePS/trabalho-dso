import PySimpleGUI as sg
from datetime import date


class TelaMenuRelatorios:
    def __init__(self):
        self.__window = None
        sg.ChangeLookAndFeel("Light Gray")

    def abre_tela(self):
        self.tela_principal()
        button, values = self.open()

        if button in (None, "Cancelar") or values["0"]:
            opcao_escolhida = 0
        elif values["1"]:
            opcao_escolhida = 1
        elif values["2"]:
            opcao_escolhida = 2
        elif values["3"]:
            opcao_escolhida = 3

        self.close()
        return opcao_escolhida

    def tela_principal(self):
        layout = [
            [sg.Radio("Animais disponíveis para adoção.", "Radio1", key="1")],
            [sg.Radio("Adoções de animais, filtrada por período.", "Radio1", key="2")],
            [sg.Radio("Doações de animais, filtrada por período.", "Radio1", key="3")],
            [
                sg.Radio(
                    "Retornar para o menu principal.", "Radio1", default=True, key="0"
                )
            ],
            [sg.Push(), sg.Button("Confirmar"), sg.Cancel("Cancelar")],
        ]
        self.__window = sg.Window("Menu de Relatórios", layout)

    def pega_periodo(self):
        layout = [
            [
                sg.Text("Período inicial (exemplo: 31/12/1999):"),
                sg.Push(),
                sg.InputText("", key="periodo_inicial"),
            ],
            [
                sg.Text("Período final (exemplo: 31/12/1999):"),
                sg.Push(),
                sg.InputText("", key="periodo_final"),
            ],
            [sg.Push(), sg.Button("Confirmar"), sg.Cancel("Cancelar")],
        ]
        self.__window = sg.Window("Seleção de período", layout)
        button, values = self.open()
        entrada_invalida = False

        if button in (None, "Cancelar"):
            self.close()
            return

        try:
            data_inicial = [int(x) for x in values["periodo_inicial"].split("/")]
            periodo_inicial = date(data_inicial[2], data_inicial[1], data_inicial[0])
            data_final = [int(x) for x in values["periodo_final"].split("/")]
            periodo_final = date(data_final[2], data_final[1], data_final[0])
        except:
            sg.popup_error("Data inválida!")
            entrada_invalida = True

        self.close()
        if not entrada_invalida:
            return {"inicial": periodo_inicial, "final": periodo_final}

    def mensagem(self, mensagem: str):
        sg.Popup("", mensagem)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()
