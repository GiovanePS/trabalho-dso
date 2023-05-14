from telas.tela_adotante import TelaAdotante
from entidades.adotante import Adotante
import os


class ControladorAdotante:
    def __init__(self, controlador_sistema):
        self.__adotantes = []
        self.__tela_adotante = TelaAdotante()
        self.__controlador_sistema = controlador_sistema

    @property
    def adotantes(self):
        return self.__adotantes

    def pega_adotante_por_cpf(self, cpf):
        for adotante in self.__adotantes:
            if adotante.cpf == cpf:
                return adotante
        return None

    def verificar_doador(self, cpf):
        for doador in self.__controlador_sistema.controlador_doador.doadores:
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
        self.__tela_adotante.mensagem("Cadastro de adotante.")
        dados_adotante = self.__tela_adotante.pega_dados_adotante()
        os.system('cls')
        if self.verificar_doador(dados_adotante["cpf"]):
            self.__tela_adotante.mensagem(
                "Não foi possível cadastrar esta pessoa. "
                "Essa pessoa já está cadastrada como doadora.\n")
            return
        if self.verificar_de_menor(dados_adotante["data_nascimento"]):
            self.__tela_adotante.mensagem(
                "Não foi possível cadastrar esta pessoa. "
                "Somente pessoas maiores de 18 anos podem ser adotantes.\n")
            return

        adotante = Adotante(dados_adotante["cpf"],
                            dados_adotante["nome"],
                            dados_adotante["data_nascimento"],
                            dados_adotante["endereco"],
                            dados_adotante["tipo_habitacao"],
                            dados_adotante["tem_animais"])
        self.__adotantes.append(adotante)
        self.__tela_adotante.mensagem("Adotante cadastrado com sucesso!")
        print()

    def alterar_adotante(self):
        self.__tela_adotante.mensagem("Alteração cadastral de adotante.")
        cpf = self.__tela_adotante.seleciona_cpf()
        adotante = self.pega_adotante_por_cpf(cpf)
        if isinstance(adotante, Adotante):
            novos_dados_adotante = self.__tela_adotante.pega_dados_adotante()
            adotante.cpf = novos_dados_adotante["cpf"]
            adotante.nome = novos_dados_adotante["nome"],
            adotante.data_nascimento = novos_dados_adotante["data_nascimento"],
            adotante.endereco = novos_dados_adotante["endereco"],
            adotante.tipo_habitacao = novos_dados_adotante["tipo_habitacao"],
            adotante.tem_animais = novos_dados_adotante["tem_animais"]
            os.system('cls')
            self.__tela_adotante.mensagem("Alteração realizada com sucesso!")
        else:
            os.system('cls')
            self.__tela_adotante.mensagem("Adotante inexistente no sistema.")
        print()

    def excluir_adotante(self):
        self.__tela_adotante.mensagem("Exclusão de adotante do sistema.")
        cpf = self.__tela_adotante.seleciona_cpf()
        adotante = self.pega_adotante_por_cpf(cpf)
        os.system('cls')
        if isinstance(adotante, Adotante):
            self.__adotantes.remove(adotante)
            self.__tela_adotante.mensagem("Adotante removido com sucesso!")
        else:
            self.__tela_adotante.mensagem("Adotante inexistente no sistema.")
        print()

    def listar_adotantes(self):
        if len(self.__adotantes) != 0:
            self.__tela_adotante.mensagem("Lista de adotantes:")
            for adotante in self.__adotantes:
                self.__tela_adotante.mostra_adotante(adotante)
        else:
            self.__tela_adotante.mensagem(
                "Não há adotantes cadastrados no sistema.")
        print()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_adotante, 2: self.alterar_adotante,
                        3: self.excluir_adotante, 4: self.listar_adotantes,
                        0: "Retornar para menu principal."}

        while True:
            opcao = self.__tela_adotante.abre_tela()
            if opcao == 0:
                return
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()
