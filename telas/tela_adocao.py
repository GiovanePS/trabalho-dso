from exceptions.valor_invalido_exception import ValorInvalido
import os
from datetime import date
from utils.cpf_validador import cpf_validador
import PySimpleGUI as sg

class TelaAdocao:
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
            [sg.Radio("Registrar adoção.", 'Radio1', key='1')],
            [sg.Radio("Alterar adoção.", 'Radio1', key='2')],
            [sg.Radio("Excluir adoção.", 'Radio1', key='3')],
            [sg.Radio("Listar adoções.", 'Radio1', key='4')],
            [sg.Radio("Retornar para o menu principal.", 'Radio1', default=True, key='0')],
            [sg.Push(), sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window("Menu de adoções", layout, finalize=True)


    def pega_dados_adocao(self):
        width_size = 30
        height_size = 1
        layout = [
            [sg.Text("Data da adoção (Exemplo: 31/12/1999):", size=(width_size, height_size)), sg.InputText('', key='data_adocao')],
            [sg.Text("Código do animal:", size=(width_size, height_size)),sg.InputText('', key='codigo_animal')],
            [sg.Text("CPF do adotante:", size=(width_size, height_size)), sg.InputText('', key='cpf_adotante')],
            [sg.Push(), sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        self.__window = sg.Window("Dados da Adoção", layout)
        button, values = self.open()
        entrada_invalida = False

        if button in (None, 'Cancelar'):
            self.close()
            return

        try:
            data = [int(x) for x in values['data_adocao'].split('/')]
            data_adocao = date(data[2], data[1], data[0])
        except:
            sg.popup_error("Data inválida!")
            entrada_invalida = True
        
        if values['codigo_animal'].isnumeric():
                pass
        else:
            sg.popup_error("Código deve ser um número inteiro!")
            entrada_invalida = True

        if not cpf_validador(values['cpf_adotante']):
            sg.popup_error("CPF Inválido.")
            entrada_invalida = True

        self.close()
        if entrada_invalida:
            return
        else:
            return {
                "data_adocao": data_adocao,
                "codigo_animal": values['codigo_animal'],
                "cpf_adotante": values['cpf_adotante']
            }


    def mostra_adocao(self, adocao):
        print("Codigo da adoção:", adocao.id_adocao)
        print("Data da adoção:", adocao.data_adocao)
        print(
            "Nome/Código do animal:",
            f'{adocao.animal_adotado.nome} / {adocao.animal_adotado.codigo}',
        )
        print(
            "Nome/CPF do adotante:",
            f'{adocao.adotante.nome} / {adocao.adotante.cpf}',
        )
        print("Termo de responsabilidade assinado:", adocao.assinatura)
        print("\n")

    def seleciona_adocao(self):
        layout = [
            [sg.Text("Código da adoção que deseja selecionar: "), sg.InputText('', key='codigo')],
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

    def pega_assinatura(self):
        width_size = 30
        height_size = 1
        layout = [
            [sg.Text("Assinar termo de responsabilidade:", size=(width_size, height_size)), sg.Radio("Sim", 'Radio1', default=True, key='sim'), sg.Radio("Não", 'Radio1', key='gato')],
            [sg.Push(), sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window("Termo de responsabilidade", layout)
        button, values = self.open()

        if button in (None, 'Cancelar'):
            self.close()
            return

        if values['sim']:
            values['a'] = True
        else:
            values['a'] = False

        self.close()
        return {
            "assinatura": values['a'],
        }


    def pega_dados_adocao_alterar(self):
        width_size = 30
        height_size = 1
        layout = [
            [sg.Text("Data da adoção (Exemplo: 31/12/1999):", size=(width_size, height_size)), sg.InputText('', key='data_adocao')],
            [sg.Text("Código do animal:", size=(width_size, height_size)),sg.InputText('', key='codigo_animal')],
            [sg.Text("Nome do animal:", size=(width_size, height_size)),sg.InputText('', key='nome_animal')],
            [sg.Text("CPF do adotante:", size=(width_size, height_size)), sg.InputText('', key='cpf_adotante')],
            [sg.Text("Nome do adotante:", size=(width_size, height_size)), sg.InputText('', key='nome_adotante')],
            [sg.Push(), sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        self.__window = sg.Window("Dados da Adoção", layout)
        button, values = self.open()
        entrada_invalida = False

        if button in (None, 'Cancelar'):
            self.close()
            return

        try:
            data = [int(x) for x in '12/02/2004'.split('/')]
            data_adocao = date(data[2], data[1], data[0])
        except:
            sg.popup_error("Data inválida!")
            entrada_invalida = True
        
        if values['codigo_animal'].isnumeric():
                pass
        else:
            sg.popup_error("Código deve ser um número inteiro!")
            entrada_invalida = True

        if not cpf_validador(values['cpf_adotante']):
            sg.popup_error("CPF Inválido.")
            entrada_invalida = True

        self.close()
        if entrada_invalida:
            return
        else:
            return {
                "data_doacao": data_adocao,
                "codigo_animal": values['codigo_animal'],
                "nome_animal": values['nome_animal'],
                "cpf_adotante": values['cpf_adotante'],
                "nome_adotante": values['nome_adotante']
            }



    def mostra_mensagem(self, mensagem: str):
        sg.Popup("", mensagem)

    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def close(self):
        self.__window.Close()
