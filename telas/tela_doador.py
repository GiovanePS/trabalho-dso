import PySimpleGUI as sg
from utils.cpf_validador import cpf_validador
from datetime import date


class TelaDoador:
    def __init__(self):
        self.__window = None
        sg.ChangeLookAndFeel('Light Gray')

    def abre_tela(self):
        self.tela_principal()
        button, values = self.open()

        if button in (None, 'Cancelar') or values['0']:
            opcao_escolhida = 0
        elif values['1']:
            opcao_escolhida = 1
        elif values['2']:
            opcao_escolhida = 2
        elif values['3']:
            opcao_escolhida = 3
        elif values['4']:
            opcao_escolhida = 4
        
        self.close()
        return opcao_escolhida

    def tela_principal(self):
        layout = [
            [sg.Radio("Incluir doador.", 'Radio1', key='1')],
            [sg.Radio("Alterar doador.", 'Radio1', key='2')],
            [sg.Radio("Excluir doador.", 'Radio1', key='3')],
            [sg.Radio("Listar doadores.", 'Radio1', key='4')],
            [sg.Radio("Retornar para o menu principal.", 'Radio1', default=True, key='0')],
            [sg.Push(), sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Menu de doadores', layout, finalize=True)
        self.__window.set_min_size((300, 200))

    def pega_dados_doador(self):
        width_size = 32
        height_size = 1
        layout = [
            [sg.Text("CPF:", size=(width_size, height_size)), sg.InputText('', key='cpf')],
            [sg.Text("Nome:", size=(width_size, height_size)), sg.InputText('', key='nome')],
            [sg.Text("Data de nascimento (Exemplo: 31/12/1999):", size=(width_size, height_size)), sg.InputText('', key='data_nascimento')],
            [sg.Text("Endereço:", size=(width_size, height_size)), sg.InputText('', key='endereco')],
            [sg.Push(), sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Dados do Doador', layout)
        button, values = self.open()
        entrada_invalida = False

        if button in (None, 'Cancelar'):
            self.close()
            return
        
        if not cpf_validador(values['cpf']):
            sg.popup_error("CPF Inválido.")
            entrada_invalida = True

        try:
            data = [int(x) for x in values['data_nascimento'].split('/')]
            data_nascimento = date(data[2], data[1], data[0])
        except:
            sg.popup_error("Data inválida!")
            entrada_invalida = True

        self.close()
        if entrada_invalida:
            return
        else:
            return {
                "cpf": values['cpf'],
                "nome": values['nome'],
                "data_nascimento": data_nascimento,
                "endereco": values['endereco']
            }

    def pega_cpf(self):
        layout = [
            [sg.Text("CPF: "), sg.InputText('', key='cpf')],
            [sg.Push(), sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window("Selecionar doador por CPF", layout)
        button, values = self.open()

        if button in (None, 'Cancelar'):
            self.close()
            return

        if not cpf_validador(values['cpf']):
            sg.popup_error("CPF Inválido.")
            self.close()
            return

        self.close()
        return values['cpf']

    def mostra_doador(self, dados_doadores: list):
        string_todos_doadores = ""
        for doador in dados_doadores:
            string_todos_doadores += f"{doador['cpf']} - {doador['nome']}, {doador['data_nascimento'].strftime('%d/%m/%Y')}\n"
            string_todos_doadores += f"\tEndereço: {doador['endereco']}.\n\n"

        width_size = 50
        height_size = 20
        layout = [
            [sg.Text("Lista de doadores:")],
            [sg.Multiline(string_todos_doadores, size=(width_size, height_size), disabled=True, text_color='#000', background_color='#FFF')],
            [sg.Push(), sg.Button("Ok"), sg.Push()],
        ]

        self.__window = sg.Window("Lista de doadores", layout, finalize=True)

        while True:
            button, values = self.open()
            if button in (None, 'Ok'):
                break

        self.close()

    def mensagem(self, mensagem: str):
        sg.Popup("", mensagem)

    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def close(self):
        self.__window.Close()