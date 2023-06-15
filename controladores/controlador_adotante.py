from telas.tela_adotante import TelaAdotante
from entidades.adotante import Adotante
from DAOs.adotante_dao import AdotanteDAO


class ControladorAdotante:
    def __init__(self, controlador_sistema):
        self.__adotante_DAO = AdotanteDAO()
        self.__tela_adotante = TelaAdotante()
        self.__controlador_sistema = controlador_sistema

    @property
    def adotantes(self):
        return self.__adotante_DAO.get_all()

    def pega_adotante_por_cpf(self, cpf):
        for adotante in self.__adotante_DAO.get_all():
            if adotante.cpf == cpf:
                return adotante
        return None

    def verificar_doador(self, cpf):
        for doador in self.__controlador_sistema.controlador_doador.doadores: #RESOLVER QUANDO FOR FAZER DAO DE DOADORES
            if doador.cpf == cpf:
                return True
        return False

    def verificar_de_menor(self, data_nascimento):
        from datetime import datetime

        if datetime.now().year - data_nascimento.year < 18:
            return True
        else:
            return False

    def incluir_adotante(self):
        dados_adotante = self.__tela_adotante.pega_dados_adotante()
        if dados_adotante is None:
            self.__tela_adotante.mensagem("Adotante não cadastrado.")
            return

        if self.verificar_doador(dados_adotante["cpf"]):
            self.__tela_adotante.mensagem(
                "Não foi possível cadastrar esta pessoa. "
                "Essa pessoa já está cadastrada como doadora."
            )
            return
        if self.verificar_de_menor(dados_adotante["data_nascimento"]):
            self.__tela_adotante.mensagem(
                "Não foi possível cadastrar esta pessoa. "
                "Somente pessoas maiores de 18 anos podem ser adotantes."
            )
            return

        adotante = Adotante(
            dados_adotante["cpf"],
            dados_adotante["nome"],
            dados_adotante["data_nascimento"],
            dados_adotante["endereco"],
            dados_adotante["tipo_habitacao"],
            dados_adotante["tem_animais"],
        )
        self.__adotante_DAO.add(adotante)
        self.__tela_adotante.mensagem("Adotante cadastrado com sucesso!")

    def alterar_adotante(self):
        cpf = self.__tela_adotante.seleciona_cpf()
        adotante = self.pega_adotante_por_cpf(cpf)
        if isinstance(adotante, Adotante):
            novos_dados_adotante = self.__tela_adotante.pega_dados_adotante()
            if novos_dados_adotante is None:
                self.__tela_adotante.mensagem("Adotante não alterado.")
                return

            if self.verificar_doador(novos_dados_adotante["cpf"]):
                self.__tela_adotante.mensagem(
                    "Não foi possível alterar o cadastro desta pessoa. "
                    "Este novo CPF já está cadastrado como doador."
                )
                return

            if adotante.cpf != novos_dados_adotante["cpf"]: # OPERAÇÃO PARA QUE ALTERAÇÃO DA KEY SEJA POSSÍVEL.
                key_antiga = adotante.cpf
                adotante = self.__adotante_DAO.get(adotante.cpf)
                self.__adotante_DAO.remove(key_antiga)
                adotante.cpf = novos_dados_adotante["cpf"]
                self.__adotante_DAO.add(adotante)
            adotante.nome = novos_dados_adotante["nome"]
            adotante.data_nascimento = novos_dados_adotante["data_nascimento"]
            adotante.endereco = novos_dados_adotante["endereco"]
            adotante.tipo_habitacao = novos_dados_adotante["tipo_habitacao"]
            adotante.tem_animais = novos_dados_adotante["tem_animais"]
            self.__adotante_DAO.update(adotante)
            self.__tela_adotante.mensagem("Alteração realizada com sucesso!")
        else:
            self.__tela_adotante.mensagem("Adotante inexistente no sistema.")

    def excluir_adotante(self):
        cpf = self.__tela_adotante.seleciona_cpf()
        adotante = self.pega_adotante_por_cpf(cpf)
        if isinstance(adotante, Adotante):
            self.__adotante_DAO.remove(adotante.cpf)
            self.__tela_adotante.mensagem("Adotante removido com sucesso!")
        else:
            self.__tela_adotante.mensagem("Adotante inexistente no sistema.")

    def listar_adotantes(self):
        if len(self.__adotante_DAO.get_all()) != 0:
            for adotante in self.__adotante_DAO.get_all():
                self.__tela_adotante.mostra_adotante(adotante)
        else:
            self.__tela_adotante.mensagem(
                "Ainda não há adotantes no sistema.")

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_adotante,
            2: self.alterar_adotante,
            3: self.excluir_adotante,
            4: self.listar_adotantes,
            0: "Retornar para menu principal.",
        }

        while True:
            opcao = self.__tela_adotante.abre_tela()
            if opcao == 0:
                return
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()
