import PySimpleGUI as sg


class TelaAnimal:
    def __init__(self):
        self.__window = None
        sg.ChangeLookAndFeel('Light Gray')

    def abre_tela(self):
        self.tela_principal()
        button, values = self.open()

        if button in (None, 'Cancelar') or values['0']:
            opcao_escolhida = 0
        elif values['1']:
            opcao_escolhida = 1 # Incluir animal somente através de uma doação.
        elif values['2']:
            opcao_escolhida = 2
        elif values['3']:
            opcao_escolhida = 3
        elif values['4']:
            opcao_escolhida = 4
        self.close()
        return opcao_escolhida

    def pega_dados_animal(self):
        width_size = 1
        height_size = 1
        layout = [
            [sg.Text("Nome do animal:"), sg.InputText('', key='nome')],
            [sg.Text("Tipo:"), sg.Radio("Cachorro"), sg.Radio("Gato")],
        ]

    def tela_principal(self):
        layout = [
            [sg.Radio("Incluir animal.", 'Radio1', key='1')],
            [sg.Radio("Alterar animal.", 'Radio1', key='2')],
            [sg.Radio("Excluir animal.", 'Radio1', key='3')],
            [sg.Radio("Listar animais.", 'Radio1', key='4')],
            [sg.Radio("Retornar para o menu principal.", 'Radio1', key='0')],
            [sg.Push(), sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window("Menu de animais", layout, finalize=True)
        self.__window.set_min_size((300, 200))

    def mostra_animal(self, dados_animais: list):
        string_todos_animais = ""
        for animal in dados_animais:
            string_todos_animais += f"{animal['codigo']} - {animal['nome']}, " \
                f"{animal['tipo']}, {animal['raca']}"
            string_todos_animais = f", {animal['tamanho']}.\n" if animal['tipo'] == "Cachorro" else ".\n"

            string_todos_animais += "Vacinas: "
            if len(animal['vacinas']) > 0:
                vacinas = ", ".join(animal['vacinas'])
                string_todos_animais += f"{vacinas}."
            else:
                string_todos_animais += "nenhuma vacina cadastrada.\n"

            if animal['pode_ser_adotado'] and not animal['foi_adotado']:
                string_todos_animais += "   Disponível para adoção: Sim.\n\n"
            else:
                string_todos_animais += "   Disponível para adoção: Não.\n\n"

    def seleciona_codigo_animal(self):
        layout = [
            [sg.Text("Código: "), sg.InputText('', key='codigo')],
            [sg.Push(), sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window("Selecionar código de um animal", layout)
        button, values = self.open()

        if button in (None, 'Cancelar'):
            self.close()
            return

        try:
            values['codigo'] = int(values['codigo'])
        except:
            sg.popup_error()
            self.close()
            return

        self.close()
        return values['codigo']

    def mensagem(self, mensagem: str):
        sg.Popup("", mensagem)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()
