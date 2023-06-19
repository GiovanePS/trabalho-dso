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
        # elif values['1']:
        #     opcao_escolhida = 1 # Incluir animal somente através de uma doação.
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
            # [sg.Radio("Incluir animal.", 'Radio1', key='1')],
            [sg.Radio("Alterar animal.", 'Radio1', key='2')],
            [sg.Radio("Excluir animal.", 'Radio1', key='3')],
            [sg.Radio("Listar animais.", 'Radio1', key='4')],
            [sg.Radio("Retornar para o menu principal.", 'Radio1', default=True, key='0')],
            [sg.Push(), sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window("Menu de animais", layout, finalize=True)
        self.__window.set_min_size((300, 200))

    def pega_dados_animal(self):
        width_size = 20
        height_size = 1
        layout = [
            [sg.Text("Nome do animal:", size=(width_size, height_size)), sg.InputText('', key='nome')],
            [sg.Text("Tipo:", size=(width_size, height_size)), sg.Radio("Cachorro", 'Radio1', default=True, key='cachorro'), sg.Radio("Gato", 'Radio1', key='gato')],
            [sg.Text("Raça:", size=(width_size, height_size)), sg.InputText('', key='raca')],
            [sg.Text("Tamanho (se for cachorro):", size=(width_size, height_size)), sg.Combo(("Pequeno", "Médio", "Grande"), readonly=True, default_value="Pequeno", key='tamanho')],
            [sg.Push(), sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window("Dados do animal", layout)
        button, values = self.open()

        if button in (None, 'Cancelar'):
            self.close()
            return

        if values['cachorro']:
            values['tipo'] = "cachorro"
        else:
            values['tipo'] = "gato"
            values['tamanho'] = None

        self.close()
        return {
            "nome": values['nome'],
            "tipo": values['tipo'],
            "raca": values['raca'],
            "tamanho": values['tamanho']
        }

    def mostra_animal(self, dados_animais: list):
        string_todos_animais = ""
        for animal in dados_animais:
            string_todos_animais += f"{animal['codigo']} - {animal['nome']}, " \
                f"{animal['tipo']}, {animal['raca']}"
            string_todos_animais += f", {animal['tamanho']}.\n" if animal['tipo'] == "Cachorro" else ".\n"

            string_todos_animais += "Vacinas: "
            if len(animal['vacinas']) > 0:
                vacinas = ", ".join(animal['vacinas'])
                string_todos_animais += f"{vacinas}."
            else:
                string_todos_animais += "nenhuma vacina cadastrada.\n"

            if animal['pode_ser_adotado'] and not animal['foi_adotado']:
                string_todos_animais += "   Disponível para adoção: Sim.\n\n"
            elif animal['pode_ser_adotado'] and animal['foi_adotado']:
                string_todos_animais += "   Disponível para adoção: Não, pois já foi adotado.\n\n"
            else:
                string_todos_animais += "   Disponível para adoção: Não, pois não tem as vacinas necessárias.\n\n"

        sg.Popup("Lista de animais (código, nome, tipo, raça, tamanho):", string_todos_animais)

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
