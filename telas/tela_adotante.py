import PySimpleGUI as sg


class TelaAdotante:
    def __init__(self):
        self.__window = None
        sg.ChangeLookAndFeel('Light Gray')

    def abre_tela(self):
        self.tela_principal()
        button, values = self.open()
        if values['1']:
            opcao_escolhida = 1
        elif values['2']:
            opcao_escolhida = 2
        elif values['3']:
            opcao_escolhida = 3
        elif values['4']:
            opcao_escolhida = 4
        elif values['0'] or button in (None, 'Cancelar'):
            opcao_escolhida = 0
        self.close()
        return opcao_escolhida

    def tela_principal(self):
        layout = [
            [sg.Text("Escolha uma opção:")],
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
        layout = [
            [sg.Text("CPF:", size=(32, 1)), sg.InputText('', key='cpf')],
            [sg.Text("Nome:", size=(32, 1)), sg.InputText('', key='nome')],
            [sg.Text("Data de nascimento (Exemplo: 31/12/1999):", size=(32, 1)), sg.InputText('', key='data_nascimento')],
            [sg.Text("Endereço:", size=(32, 1)), sg.InputText('', key='endereco')],
            [sg.Text("Tipo de habitação:", size=(32, 1)), sg.Combo(("Casa pequena", "Casa média", "Casa grande", "Apartamento pequeno", "Apartamento médio", "Apartamento grande"))],
            [sg.Text("Tem animais?", size=(32, 1)), sg.Radio("Não", 'Radio1', key=0), sg.Radio("Sim", 'Radio1', key=1)],
            [sg.Push(), sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Dados do Adotante', layout)
        button, values = self.open()
        if button == 'Cancelar':
            self.close()
            return

        self.close()
        return {"nome": values['nome'],
                "telefone": values['telefone'],
                "cpf": values['cpf']
            }

    def mostra_adotante(self):
        ...

    def mensagem(self, mensagem: str):
        sg.Popup("", mensagem)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

var = TelaAdotante()
var.pega_dados_adotante()