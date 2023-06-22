from exceptions.valor_invalido_exception import ValorInvalido
import os
from utils.cpf_validador import cpf_validador
from datetime import date
import PySimpleGUI as sg


class TelaDoacao:
    def __init__(self):
        self.__window = None
        sg.ChangeLookAndFeel('Light Gray')

    def abre_tela(self):
        self.tela_opcoes()
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

    def tela_opcoes(self):
        layout = [
            [sg.Radio("Registrar doação.", 'Radio1', key='1')],
            [sg.Radio("Alterar doação.", 'Radio1', key='2')],
            [sg.Radio("Excluir doação.", 'Radio1', key='3')],
            [sg.Radio("Listar doações.", 'Radio1', key='4')],
            [sg.Radio("Retornar para o menu principal.", 'Radio1', default=True, key='0')],
            [sg.Push(), sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window("Menu de doações", layout, finalize=True)

    def pega_dados_doacao(self):
        width_size = 30
        height_size = 1
        layout = [
            [sg.Text("Data da doação (Exemplo: 31/12/1999):", size=(width_size, height_size)), sg.InputText('', key='data_doacao')],
            [sg.Text("Código do animal:", size=(width_size, height_size)),sg.InputText('', key='codigo_animal')],
            [sg.Text("CPF do doador:", size=(width_size, height_size)), sg.InputText('', key='cpf_doador')],
            [sg.Text("Motivo da doação:", size=(width_size, height_size)), sg.InputText('', key='motivo')],
            [sg.Push(), sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        self.__window = sg.Window("Dados da Doação", layout)
        button, values = self.open()
        entrada_invalida = False

        if button in (None, 'Cancelar'):
            self.close()
            return

        try:
            data = [int(x) for x in values['data_doacao'].split('/')]
            data_doacao = date(data[2], data[1], data[0])
        except:
            sg.popup_error("Data inválida!")
            entrada_invalida = True
        
        if values['codigo_animal'].isnumeric():
                pass
        else:
            sg.popup_error("Código deve ser um número inteiro!")
            entrada_invalida = True

        if not cpf_validador(values['cpf_doador']):
            sg.popup_error("CPF Inválido.")
            entrada_invalida = True

        self.close()
        if entrada_invalida:
            return
        else:
            return {
                "data_doacao": data_doacao,
                "codigo_animal": values['codigo_animal'],
                "cpf_doador": values['cpf_doador'],
                "motivo": values['motivo']
            }

    def mostra_doacao(self, dados_doacoes:list):
        string_todas_doacoes = ""
        for doacao in dados_doacoes:
            string_todas_doacoes += f"Código da doação: {doacao['id_doacao']} \n"
            string_todas_doacoes += f"Data da doação: {doacao['data_doacao']} \n"
            string_todas_doacoes += f'Nome/CPF do doador: {doacao["doador"].nome} / {doacao["doador"].cpf} \n'
            string_todas_doacoes += f'Nome/Código do animal: {doacao["animal"].nome} / {doacao["animal"].codigo} \n'
            string_todas_doacoes += f"Motivo da doação: {doacao['motivo']} \n"

        sg.Popup("Lista de doações:", string_todas_doacoes)

    def seleciona_doacao(self):
        layout = [
            [sg.Text("Código da doação que deseja selecionar: "), sg.InputText('', key='codigo')],
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

    
    def pega_dados_doacao_altera(self):

        width_size = 30
        height_size = 1
        layout = [
            [sg.Text("Data da doação (Exemplo: 31/12/1999):", size=(width_size, height_size)), sg.InputText('', key='data_doacao')],
            [sg.Text("Código do animal:", size=(width_size, height_size)),sg.InputText('', key='codigo_animal')],
            [sg.Text("Nome do animal:", size=(width_size, height_size)),sg.InputText('', key='nome_animal')],
            [sg.Text("CPF do doador:", size=(width_size, height_size)), sg.InputText('', key='cpf_doador')],
            [sg.Text("Nome do doador:", size=(width_size, height_size)), sg.InputText('', key='nome_doador')],
            [sg.Text("Motivo da doação:", size=(width_size, height_size)), sg.InputText('', key='motivo')],
            [sg.Push(), sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        self.__window = sg.Window("Dados da Doação", layout)
        button, values = self.open()
        entrada_invalida = False

        if button in (None, 'Cancelar'):
            self.close()
            return

        try:
            data = [int(x) for x in '12/02/2004'.split('/')]
            data_doacao = date(data[2], data[1], data[0])
        except:
            sg.popup_error("Data inválida!")
            entrada_invalida = True
        
        if values['codigo_animal'].isnumeric():
                pass
        else:
            sg.popup_error("Código deve ser um número inteiro!")
            entrada_invalida = True

        if not cpf_validador(values['cpf_doador']):
            sg.popup_error("CPF Inválido.")
            entrada_invalida = True

        self.close()
        if entrada_invalida:
            return
        else:
            return {
                "data_doacao": data_doacao,
                "codigo_animal": values['codigo_animal'],
                "nome_animal": values['nome_animal'],
                "cpf_doador": values['cpf_doador'],
                "nome_doador": values['nome_doador'],
                "motivo": values['motivo']
            }


    def mensagem(self, mensagem: str):
        sg.Popup("", mensagem)

    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def close(self):
        self.__window.Close()
