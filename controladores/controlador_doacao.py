from telas.tela_doacao import TelaDoacao
from entidades.doacao import Doacao
from DAOs.doacao_dao import DoacaoDAO


class ControladorDoacao:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__doacao_DAO= DoacaoDAO()
        self.__tela_doacao = TelaDoacao()
        self.__id = 0

    @property
    def doacoes(self):
        return self.__doacao_DAO.get_all()

    @property
    def tela_doacao(self):
        return self.__tela_doacao

    def pega_doacao_por_codigo(self, codigo: int):
        for doacao in self.__doacao_DAO.get_all():
            if int(doacao.id_doacao) == int(codigo):
                return doacao

    def incluir_doacao(self):
        if len(self.__controlador_sistema.controlador_doador.doadores) != 0:
            dados_doacao = self.__tela_doacao.pega_dados_doacao()
            if dados_doacao is None:
                self.__tela_doacao.mensagem("Doação não cadastrada.")
                return

            doador = self.__controlador_sistema.controlador_doador.pega_doador_por_cpf(
                dados_doacao["cpf_doador"]
            )

            if doador is not None:
                codigo_animal_cadastrado = self.__controlador_sistema.controlador_animal.incluir_animal()
                if codigo_animal_cadastrado is None:
                    self.__tela_doacao.mensagem("Doação não cadastrada.")
                    return

                animal = self.__controlador_sistema.controlador_animal.pegar_animal_por_codigo(
                    codigo_animal_cadastrado
                )
                try:
                    self.__id = int(list(self.__doacao_DAO.get_all())[-1].id_doacao) + 1
                except IndexError:
                    self.__id = 1
                doacao = Doacao(
                    dados_doacao["data_doacao"],
                    animal,
                    doador,
                    dados_doacao["motivo"],
                    self.__id,
                )
                self.__doacao_DAO.add(doacao)
                self.__tela_doacao.mensagem("Doação cadastrada com sucesso.")
            else:
                self.__tela_doacao.mensagem("Dados inválidos!")
        else:
            self.tela_doacao.mensagem("Ainda não há doadores no sistema.")

    def alterar_doacao(self):
        id_doacao = self.__tela_doacao.seleciona_doacao()
        if id_doacao is None:
            self.__tela_doacao.mensagem("Doação não alterada.")
            return

        doacao = self.pega_doacao_por_codigo(id_doacao)

        if doacao is not None:
            novos_dados_doacao = self.__tela_doacao.pega_dados_doacao_altera()
            if novos_dados_doacao is None:
                self.__tela_doacao.mensagem("Doação não alterada.")
                return
            doacao.data_doacao = novos_dados_doacao["data_doacao"]
            doacao.animal.nome = novos_dados_doacao["nome_animal"]
            doacao.animal.codigo = novos_dados_doacao["codigo_animal"]
            doacao.doador.nome = novos_dados_doacao["nome_doador"]
            doacao.doador.cpf = novos_dados_doacao["cpf_doador"]
            doacao.motivo = novos_dados_doacao["motivo"]
        else:
            self.__tela_doacao.mensagem("Essa doação não existe.")

    def excluir_doacao(self):
        id_doacao = self.__tela_doacao.seleciona_doacao()
        if id_doacao is None:
            self.__tela_doacao.mensagem("Doação não excluída.")
            return

        doacao = self.pega_doacao_por_codigo(id_doacao)

        if doacao is not None:
            self.__doacao_DAO.remove(doacao.id_doacao)
            self.__tela_doacao.mensagem("Doação removida com sucesso!")
        else:
            self.__tela_doacao.mensagem("Essa doação não existe.")

    def listar_doacoes(self):
        if len(self.__doacao_DAO.get_all()) == 0:
            self.__tela_doacao.mensagem("Ainda não há doações no sistema.")
        else:
            dados_doacoes = []
            for doacao in self.__doacao_DAO.get_all():
                dados_doacoes.append({
                    "id_doacao":doacao.id_doacao,
                    "data_doacao":doacao.data_doacao,
                    "doador_nome":doacao.doador.nome,
                    "doador_cpf":doacao.doador.cpf,
                    "animal_nome":doacao.animal.nome,
                    "animal_codigo":doacao.animal.codigo,
                    "motivo":doacao.motivo,
                })
                
            self.__tela_doacao.mostra_doacao(dados_doacoes)

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_doacao,
            2: self.alterar_doacao,
            3: self.excluir_doacao,
            4: self.listar_doacoes,
            0: "Retornar para menu principal",
        }
        while True:
            opcao = self.__tela_doacao.abre_tela()
            if opcao == 0:
                return
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()
