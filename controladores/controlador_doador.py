from telas.tela_doador import TelaDoador
from entidades.doador import Doador
from DAOs.doador_dao import DoadorDAO


class ControladorDoador:
    def __init__(self, controlador_sistema):
        self.__doador_DAO = DoadorDAO()
        self.__tela_doador = TelaDoador()
        self.__controlador_sistema = controlador_sistema

    @property
    def doadores(self):
        return self.__doador_DAO.get_all()

    def pega_doador_por_cpf(self, cpf):
        for doador in self.__doador_DAO.get_all():
            if doador.cpf == cpf:
                return doador
        return None

    def verificar_adotante(self, cpf):
        for adotante in self.__controlador_sistema.controlador_adotante.adotantes:
            if adotante.cpf == cpf:
                return True
        return False

    def incluir_doador(self):
        dados_doador = self.__tela_doador.pega_dados_doador()
        if dados_doador is None:
            self.__tela_doador.mensagem("Doador não cadastrado.")
            return

        if self.verificar_adotante(dados_doador["cpf"]):
            self.__tela_doador.mensagem(
                "Não foi possível cadastrar esta pessoa. "
                "Essa pessoa já está cadastrada como adotante."
            )
            return

        doador = Doador(
            dados_doador["cpf"],
            dados_doador["nome"],
            dados_doador["data_nascimento"],
            dados_doador["endereco"],
        )
        self.__doador_DAO.add(doador)
        self.__tela_doador.mensagem("Doador cadastrado com sucesso!")

    def alterar_doador(self):
        cpf = self.__tela_doador.pega_cpf()
        doador = self.pega_doador_por_cpf(cpf)
        if isinstance(doador, Doador):
            novos_dados_doador = self.__tela_doador.pega_dados_doador()
            if novos_dados_doador is None:
                self.__tela_doador.mensagem("Doador não alterado.")
                return

            if self.verificar_adotante(novos_dados_doador["cpf"]):
                self.__tela_doador.mensagem(
                    "Não foi possível alterar o cadastro desta pessoa. "
                    "Este novo CPF já está cadastrado como doador.\n"
                )
                return
            
            if doador.cpf != novos_dados_doador["cpf"]:
                key_antiga = doador.cpf
                doador = self.__doador_DAO.get(doador.cpf)
                self.__doador_DAO.remove(key_antiga)
                doador.cpf = novos_dados_doador["cpf"]
                self.__doador_DAO.add(doador)
            doador.nome = novos_dados_doador["nome"]
            doador.data_nascimento = novos_dados_doador["data_nascimento"]
            doador.endereco = novos_dados_doador["endereco"]
            self.__doador_DAO.update(doador)
            self.__tela_doador.mensagem("Doador alterado com sucesso!")
        else:
            self.__tela_doador.mensagem("Doador inexistente no sistema.")

    def excluir_doador(self):
        cpf = self.__tela_doador.pega_cpf()
        doador = self.pega_doador_por_cpf(cpf)
        if isinstance(doador, Doador):
            self.__doador_DAO.remove(doador.cpf)
            self.__tela_doador.mensagem("Doador removido com sucesso!")
        else:
            self.__tela_doador.mensagem("Doador inexistente no sistema.")

    def listar_doadores(self):
        dados_doadores = []
        if len(self.__doador_DAO.get_all()) != 0:
            for doador in self.__doador_DAO.get_all():
                dados_doadores.append({
                    'cpf': doador.cpf,
                    'nome': doador.nome,
                    'data_nascimento': doador.data_nascimento,
                    'endereco': doador.endereco,
                })

            self.__tela_doador.mostra_doador(dados_doadores)
        else:
            self.__tela_doador.mensagem(
                "Ainda não há doadores no sistema.")

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_doador,
            2: self.alterar_doador,
            3: self.excluir_doador,
            4: self.listar_doadores,
            0: "Retornar para menu principal",
        }

        while True:
            opcao = self.__tela_doador.abre_tela()
            if opcao == 0:
                return
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()
