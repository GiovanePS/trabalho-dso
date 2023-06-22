import PySimpleGUI as sg
from datetime import date

class TelaVacinacao:
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
        elif values['5']:
            opcao_escolhida = 5

        self.close()
        return opcao_escolhida

    def tela_principal(self):
        layout = [
            [sg.Radio("Incluir vacinação.", 'Radio1', key='1')],
            [sg.Radio("Alterar vacinação.", 'Radio1', key='2')],
            [sg.Radio("Excluir vacinação.", 'Radio1', key='3')],
            [sg.Radio("Listar vacinações.", 'Radio1', key='4')],
            [sg.Radio("Ver vacinas.", 'Radio1', key='5')],
            [sg.Radio("Retornar para o menu principal.", 'Radio1', default=True, key='0')],
            [sg.Push(), sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window("Menu de vacinação", layout, finalize=True)
        self.__window.set_min_size((300, 200))

    def pega_dados_vacinacao(self):
        layout = [
            [sg.Text("Data da vacinação (Exemplo: 31/12/1999):"), sg.InputText('', key='data_vacinacao')],
            [sg.Text("Código do animal vacinado:"), sg.InputText('', key='codigo_animal_vacinado')],
            [sg.Text("Código da vacina aplicada:"), sg.InputText('', key='codigo_vacina')],
            [sg.Push(), sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window("Dados da vacinação", layout)
        button, values = self.open()
        entrada_invalida = False

        if button in (None, 'Cancelar'):
            self.close()
            return
        
        try:
            data = [int(x) for x in values['data_vacinacao'].split('/')]
            data_vacinacao = date(data[2], data[1], data[0])
        except:
            sg.popup_error("Data inválida!")
            entrada_invalida = True

        self.close()
        if entrada_invalida:
            return
        else:
            return {
                "data_vacinacao": data_vacinacao,
                "codigo_animal_vacinado": values['codigo_animal_vacinado'],
                "codigo_vacina": values['codigo_vacina']
            }

    def seleciona_vacinacao(self):
        layout = [
            [sg.Text("Código da vacinação:"), sg.InputText('', key='id_vacinacao')],
            [sg.Push(), sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window("Selecionar vacinação", layout)
        button, values = self.open()

        if button in (None, 'Cancelar'):
            self.close()
            return
        
        self.close()
        return values['id_vacinacao']

    def mostra_vacinacao(self, dados_vacinacoes: list):
        string_todas_vacinacoes = ""
        for vacinacao in dados_vacinacoes:
            string_todas_vacinacoes += f"Codigo da vacinação: {vacinacao['codigo_vacinacao']}\n"
            string_todas_vacinacoes += f"Data da vacinação: {vacinacao['data_vacinacao']}\n"
            string_todas_vacinacoes += f"Nome/Código do animal vacinado: {vacinacao['nome_animal']} / {vacinacao['codigo_animal']}\n"
            string_todas_vacinacoes += f"Nome/Código da vacina: {vacinacao['nome_vacina']} / {vacinacao['codigo_vacina']}\n\n"

        sg.Popup("Lista de vacinações", string_todas_vacinacoes)

    def mensagem(self, mensagem: str):
        sg.Popup("", mensagem)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()