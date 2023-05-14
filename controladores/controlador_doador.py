from telas.tela_doador import TelaDoador
from entidades.doador import Doador
import os


class ControladorDoador:
    def __init__(self, controlador_sistema):
        self.__doadores = []
        self.__tela_doador = TelaDoador()
        self.__controlador_sistema = controlador_sistema

    @property
    def doadores(self):
        return self.__doadores

    def pega_doador_por_cpf(self, cpf):
        for doador in self.__doadores:
            if doador.cpf == cpf:
                return doador
        return None

    def verificar_adotante(self, cpf):
        for adotante in self.__controlador_sistema.controlador_adotante.adotantes: # noqa
            if adotante.cpf == cpf:
                return True
        return False

    def incluir_doador(self):
        self.__tela_doador.mensagem("Cadastro de doador.")
        dados_doador = self.__tela_doador.pega_dados_doador()
        os.system('cls')
        if self.verificar_adotante(dados_doador["cpf"]):
            self.__tela_doador.mensagem(
                "Não foi possível cadastrar esta pessoa. "
                "Essa pessoa já está cadastrada como adotante.")
            return

        doador = Doador(dados_doador["cpf"],
                        dados_doador["nome"],
                        dados_doador["data_nascimento"],
                        dados_doador["endereco"])
        self.__doadores.append(doador)
        self.__tela_doador.mensagem("Doador cadastrado com sucesso!")
        print()

    def alterar_doador(self):
        self.__tela_doador.mensagem("Alteração cadastral de doador")
        cpf = self.__tela_doador.pega_cpf()
        doador = self.pega_doador_por_cpf(cpf)
        if isinstance(doador, Doador):
            novos_dados_doador = self.__tela_doador.pega_dados_doador()
            if self.verificar_adotante(novos_dados_doador["cpf"]):
                self.__tela_doador.mensagem(
                    "Não foi possível alterar o cadastro desta pessoa. "
                    "Este novo CPF já está cadastrado como doador.\n")
                return
            doador.cpf = novos_dados_doador["cpf"]
            doador.nome = novos_dados_doador["nome"]
            doador.data_nascimento = novos_dados_doador["data_nascimento"]
            doador.endereco = novos_dados_doador["endereco"]
            os.system('cls')
            self.__tela_doador.mensagem("Alteração realizada com sucesso!")
        else:
            os.system('cls')
            self.__tela_doador.mensagem("Doador inexistente no sistema.")
        print()

    def excluir_doador(self):
        self.__tela_doador.mensagem("Exclusão de doador do sistema.")
        cpf = self.__tela_doador.pega_cpf()
        doador = self.pega_doador_por_cpf(cpf)
        os.system('cls')
        if isinstance(doador, Doador):
            self.__doadores.remove(doador)
            self.__tela_doador.mensagem("Doador removido com sucesso!")
        else:
            self.__tela_doador.mensagem("Doador inexistente no sistema.")
        print()

    def listar_doadores(self):
        if len(self.__doadores) != 0:
            self.__tela_doador.mensagem("Lista de doadores:")
            for doador in self.__doadores:
                self.__tela_doador.mostra_doador(doador)
        else:
            self.__tela_doador.mensagem(
                "Ainda não há doadores no sistema. Voce deve cadastrar primeiro!")
            self.__controlador_sistema.abre_tela()
        print()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_doador, 2: self.alterar_doador,
                        3: self.excluir_doador, 4: self.listar_doadores,
                        0: "Retornar para menu principal"}

        while True:
            opcao = self.__tela_doador.tela_opcoes()
            if opcao == 0:
                return
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()
