from telas.tela_menu_relatorios import TelaMenuRelatorios


class ControladorMenuRelatorios:
    def __init__(self, controlador_sistema):
        self.__tela_menu_relatorios = TelaMenuRelatorios()
        self.__controlador_sistema = controlador_sistema

    def animais_disponiveis_para_adocao(self):
        contador_de_animais_disponiveis = 0
        for animal in self.__controlador_sistema.controlador_animal.animais:
            if not animal.foi_adotado and animal.pode_ser_adotado:
                self.__controlador_sistema.controlador_animal.tela_animal.mostra_animal(animal)
                contador_de_animais_disponiveis += 1
        if contador_de_animais_disponiveis == 0:
            self.__tela_menu_relatorios.mensagem("Não há animais disponíveis.\n")

    def adocoes_por_periodo(self):
        periodo = self.__tela_menu_relatorios.pega_periodo()
        if periodo is None:
            return
        contador_adocoes = 0
        self.__tela_menu_relatorios.mensagem(f"Lista de adoções entre {periodo['inicial'].strftime('%d/%m/%Y')} e {periodo['final'].strftime('%d/%m/%Y')}")
        for adocao in self.__controlador_sistema.controlador_adocao.adocoes:
            if periodo['inicial'] <= adocao.data_adocao <= periodo['final']:
                self.__controlador_sistema.controlador_adocao.tela_adocao.mostra_adocao(adocao)
                contador_adocoes += 1

        if contador_adocoes == 0:
            self.__tela_menu_relatorios.mensagem("Não houveram adoções neste período.\n")

    def doacoes_por_periodo(self):
        periodo = self.__tela_menu_relatorios.pega_periodo()
        if periodo is None:
            return
        contador_doacoes = 0
        self.__tela_menu_relatorios.mensagem(f"Lista de doações entre {periodo['inicial'].strftime('%d/%m/%Y')} e {periodo['data_final'].strftime('%d/%m/%Y')}")
        for doacao in self.__controlador_sistema.controlador_doacao.doacoes:
            if periodo['inicial'] <= doacao.data_doacao <= periodo['final']:
                self.__controlador_sistema.controlador_doacao.tela_doacao.mostra_doacao(doacao)
                contador_doacoes += 1

        if contador_doacoes == 0:
            self.__tela_menu_relatorios.mensagem("Não houveram doações neste período.\n")

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
