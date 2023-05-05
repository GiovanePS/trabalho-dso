from telas.tela_doador import TelaDoador
from entidades.doador import Doador
import os


class ControladorDoador:
    def __init__(self):
        self.__doadores = []
        self.__tela_doador = TelaDoador()

    def pega_doador_por_cpf(self, cpf):
        for doador in self.__doadores:
            if doador.cpf == cpf:
                return doador
        return None

    def incluir_doador(self):
        self.__tela_doador.mensagem("Cadastro de doador.")
        dados_doador = self.__tela_doador.pega_dados_doador()
        doador = Doador(dados_doador["cpf"],
                        dados_doador["nome"],
                        dados_doador["data_nascimento"],
                        dados_doador["endereco"])
        self.__doadores.append(doador)
        os.system('cls')
        self.__tela_doador.mensagem("Doador cadastrado com sucesso!")
        print()

    def alterar_doador(self):
        self.__tela_doador.mensagem("Alteração cadastral de doador")
        cpf = self.__tela_doador.pega_cpf()
        doador = self.pega_doador_por_cpf(cpf)
        os.system('cls')
        if isinstance(doador, Doador):
            novos_dados_doador = self.__tela_doador.pega_dados_doador()
            doador.cpf = novos_dados_doador["cpf"]
            doador.nome = novos_dados_doador["nome"]
            doador.data_nascimento = novos_dados_doador["data_nascimento"]
            doador.endereco = novos_dados_doador["endereco"]
            self.__tela_doador.mensagem("Alteração realizada com sucesso!")
        else:
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
        self.__tela_doador.mensagem("Lista de doadores:")
        if len(self.__doadores) != 0:
            for doador in self.__doadores:
                self.__tela_doador.mostra_doador(doador)
        else:
            print("Não há doadores cadastrados no sistema.")
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
