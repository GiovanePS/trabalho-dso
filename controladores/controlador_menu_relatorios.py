from telas.tela_menu_relatorios import TelaMenuRelatorios


class ControladorMenuRelatorios:
    def __init__(self, controlador_sistema):
        self.__tela_menu_relatorios = TelaMenuRelatorios()
        self.__controlador_sistema = controlador_sistema

    def animais_disponiveis_para_adocao(self):
        contador_de_animais_disponiveis = 0
        for animal in self.__controlador_sistema.controlador_animal.animais:
            if not animal.foi_adotado and animal.pode_ser_adotado:
                self.__controlador_sistema.controlador_animal.tela_animal.mostra_animal(animal) # noqa
                contador_de_animais_disponiveis += 1
        if contador_de_animais_disponiveis == 0:
            print("Não há animais disponíveis.\n")

    def adocoes_por_periodo(self):
        ...

    def doacoes_por_periodo(self):
        ...

    def abre_tela(self):
        lista_opcoes = {
            1: self.animais_disponiveis_para_adocao,
            2: self.adocoes_por_periodo,
            3: self.doacoes_por_periodo,
            0: "Retornar para o menu principal",
        }

        while True:
            opcao = self.__tela_menu_relatorios.abre_tela()
            if opcao == 0:
                return
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()
