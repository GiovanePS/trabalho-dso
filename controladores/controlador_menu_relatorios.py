from telas.tela_menu_relatorios import TelaMenuRelatorios


class ControladorMenuRelatorios:
    def __init__(self, controlador_sistema):
        self.__tela_menu_relatorios = TelaMenuRelatorios()
        self.__controlador_sistema = controlador_sistema

    def animais_disponiveis_para_adocao(self):
        contador_de_animais_disponiveis = 0
        dados_animais = []
        for animal in self.__controlador_sistema.controlador_animal.animais:
            if not animal.foi_adotado and animal.pode_ser_adotado:
                dados_animais.append({
                    "codigo": animal.codigo,
                    "nome": animal.nome,
                    "tipo": animal.tipo,
                    "raca": animal.raca,
                    "tamanho": animal.tamanho,
                    "vacinas": animal.vacinas,
                    "pode_ser_adotado": animal.pode_ser_adotado,
                    "foi_adotado": animal.foi_adotado
                })
                contador_de_animais_disponiveis += 1
        if contador_de_animais_disponiveis == 0:
            self.__tela_menu_relatorios.mensagem("Não há animais disponíveis.\n")
        else:
            self.__controlador_sistema.controlador_animal.tela_animal.mostra_animal(dados_animais)

    def adocoes_por_periodo(self):
        periodo = self.__tela_menu_relatorios.pega_periodo()
        if periodo is None:
            return
        contador_adocoes = 0
        dados_adocoes = []
        for adocao in self.__controlador_sistema.controlador_adocao.adocoes:
            if periodo['inicial'] <= adocao.data_adocao <= periodo['final']:
                dados_adocoes.append({
                    "id_adocao": adocao.id_adocao,
                    "data_adocao": adocao.data_adocao,
                    "animal_adotado_nome": adocao.animal_adotado.nome,
                    "animal_adotado_codigo": adocao.animal_adotado.codigo,
                    "adotante_nome": adocao.adotante.nome,
                    "adotante_cpf": adocao.adotante.cpf,
                    "assinatura": adocao.assinatura
                })
                contador_adocoes += 1
                
        if contador_adocoes == 0:
            self.__tela_menu_relatorios.mensagem("Não houveram adoções neste período.")
            return
        else:
            self.__controlador_sistema.controlador_adocao.tela_adocao.mostra_adocao(dados_adocoes, f"Lista de adoções entre:\n{periodo['inicial'].strftime('%d/%m/%Y')} e {periodo['final'].strftime('%d/%m/%Y')}")


    def doacoes_por_periodo(self):
        periodo = self.__tela_menu_relatorios.pega_periodo()
        if periodo is None:
            return
        contador_doacoes = 0
        dados_doacoes = []
        for doacao in self.__controlador_sistema.controlador_doacao.doacoes:
            if periodo['inicial'] <= doacao.data_doacao <= periodo['final']:
                dados_doacoes.append({
                    "id_doacao":doacao.id_doacao,
                    "data_doacao":doacao.data_doacao,
                    "doador_nome":doacao.doador.nome,
                    "doador_cpf":doacao.doador.cpf,
                    "animal_nome":doacao.animal.nome,
                    "animal_codigo":doacao.animal.codigo,
                    "motivo":doacao.motivo,
                })
                contador_doacoes += 1

        if contador_doacoes == 0:
            self.__tela_menu_relatorios.mensagem("Não houveram doações neste período.")
            return
        else:
            self.__controlador_sistema.controlador_doacao.tela_doacao.mostra_doacao(dados_doacoes, f"Lista de doações entre {periodo['inicial'].strftime('%d/%m/%Y')} e {periodo['final'].strftime('%d/%m/%Y')}")

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
