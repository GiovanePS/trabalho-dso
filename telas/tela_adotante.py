import PySimpleGUI as sg
from utils.cpf_validador import cpf_validador
from datetime import date


class TelaAdotante:
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
            [sg.Radio("Incluir adotante.", 'Radio1', key='1')],
            [sg.Radio("Alterar adotante.", 'Radio1', key='2')],
            [sg.Radio("Excluir adotante.", 'Radio1', key='3')],
            [sg.Radio("Listar adotantes.", 'Radio1', key='4')],
            [sg.Radio("Retornar para o menu principal.", 'Radio1', key='0')],
            [sg.Push(), sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Menu de adotantes', layout, finalize=True) #finalize é para ser possível definir um tamanho mínimo para a janela
        self.__window.set_min_size((300, 200)) #tamanho mínimo para a janela.

    def pega_dados_adotante(self):
        width_size = 32
        height_size = 1
        layout = [
            [sg.Text("CPF:", size=(width_size, height_size)), sg.InputText('', key='cpf')],
            [sg.Text("Nome:", size=(width_size, height_size)), sg.InputText('', key='nome')],
            [sg.Text("Data de nascimento (Exemplo: 31/12/1999):", size=(width_size, height_size)), sg.InputText('', key='data_nascimento')],
            [sg.Text("Endereço:", size=(width_size, height_size)), sg.InputText('', key='endereco')],
            [sg.Text("Tipo de habitação:", size=(width_size, height_size)), sg.InputCombo(("Casa pequena", "Casa média", "Casa grande", "Apartamento pequeno", "Apartamento médio", "Apartamento grande"), readonly=True, key='tipo_habitacao')],
            [sg.Text("Tem animais?", size=(width_size, height_size)), sg.Radio("Não", 'Radio1'), sg.Radio("Sim", 'Radio1', key='tem_animais')],
            [sg.Push(), sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Dados do Adotante', layout)
        button, values = self.open()
        entrada_invalida = False

        if button == 'Cancelar':
            self.close()
            return
        
        if not cpf_validador(values['cpf']):
            sg.popup_error("CPF Inválido.")
            entrada_invalida = True

        try:
            data = [int(x) for x in '12/02/2004'.split('/')]
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
                "endereco": values['endereco'],
                "tipo_habitacao": values['tipo_habitacao'],
                "tem_animais": values['tem_animais'],
            }

    def seleciona_cpf(self):
        layout = [
            [sg.Text("CPF: "), sg.InputText('', key='cpf')],
            [sg.Push(), sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window("Selecionar adotante por CPF", layout)
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

    def mostra_adotante(self, dados_adotantes: list):
        string_todos_adotantes = ""
        for adotante in dados_adotantes:
            string_todos_adotantes += f"{adotante['cpf']} - {adotante['nome']}, {adotante['data_nascimento'].strftime('%d/%m/%Y')}\n"
            string_todos_adotantes += f"\tEndereço: {adotante['endereco']}\n\n"

        sg.Popup("Lista de adotantes", string_todos_adotantes)

    def mensagem(self, mensagem: str):
        sg.Popup("", mensagem)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()
