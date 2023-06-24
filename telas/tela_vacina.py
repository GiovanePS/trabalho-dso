from exceptions.valor_invalido_exception import ValorInvalido
from entidades.vacina import Vacina
import os
import PySimpleGUI as sg


class TelaVacina:

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
            [sg.Radio("Cadastrar vacina.", 'Radio1', key='1')],
            [sg.Radio("Alterar vacina.", 'Radio1', key='2')],
            [sg.Radio("Excluir vacina.", 'Radio1', key='3')],
            [sg.Radio("Listar vacinas.", 'Radio1', key='4')],
            [sg.Radio("Retornar para o menu principal.", 'Radio1', default=True, key='0')],
            [sg.Push(), sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window("Menu de animais", layout)

    def pega_dados_vacina(self):
        width_size = 20
        height_size = 1
        layout = [
            [sg.Text("Nome da vacina:", size=(width_size, height_size)), sg.InputCombo(("Raiva", "Leptospirose", "Hepatite Infecciosa", "Outra"), readonly=True, default_value="Outra", key='nome_vacina')],
            [sg.Text("Nome da vacina (se outra):", size=(width_size, height_size)), sg.InputText("", key='nome_outra')],
            [sg.Push(), sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window("Dados da vacina", layout)
        button, values = self.open()
        entrada_invalida = False

        if button in (None, 'Cancelar'):
            self.close()
            return
        
        if values['nome_vacina'] == 'Outra':
            if len(values['nome_outra']) != 0:
                values['nome_vacina'] == values['nome_outra']
            else:
                sg.popup_error("Digite um nome de vacina!")
                entrada_invalida = True

        self.close()
        if entrada_invalida:
            return
        else:
            return {
                "nome_vacina": values['nome_vacina'],
            }

    def mostra_vacina(self, dados_vacina:list):
        string_vacinas = ""
        for vacina in dados_vacina:
            string_vacinas += f'{vacina["codigo"]} - {vacina["nome"]} \n'

        sg.Popup("Lista de vacinas cadastradas (código - nome):", string_vacinas)

    def seleciona_codigo(self):
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
            sg.popup_error("Digite um número inteiro.")
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
