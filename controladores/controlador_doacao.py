from telas.tela_doacao import TelaDoacao
from entidades.doacao import Doacao
import os


class ControladorDoacao():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__doacoes = []
        self.__id = 0
        self.__tela_doacao = TelaDoacao()

    def pega_doacao_por_codigo(self, codigo: int):
        for doacao in self.__doacoes:
            if int(doacao.id_doacao) == int(codigo):
                return doacao

    def incluir_doacao(self):
        self.__controlador_sistema.controlador_animal.listar_animais()
        self.__controlador_sistema.controlador_doador.listar_doadores()

        dados_doacao = self.__tela_doacao.pega_dados_doacao()

        self.__tela_doacao.mensagem("Cadastro de doação:")

        animal = self.__controlador_sistema.controlador_animal.pegar_animal_por_codigo(dados_doacao["codigo_animal"]) # noqa
        doador = self.__controlador_sistema.controlador_doador.pega_doador_por_cpf(dados_doacao["cpf_doador"]) # noqa

        if (doador is not None and animal is not None):
            self.__id += 1
            doacao = Doacao(dados_doacao["data_doacao"],
                            animal, doador,
                            dados_doacao["motivo"], self.__id)
            self.__doacoes.append(doacao)
            os.system('cls')
            print("Doação cadastrada com sucesso.")
        else:
            self.__tela_doacao.mensagem("Dados inválidos!")

    def alterar_doacao(self):
        self.listar_doacoes()
        id_doacao = self.__tela_doacao.seleciona_doacao()
        doacao = self.pega_doacao_por_codigo(id_doacao)

        if (doacao is not None):
            novos_dados_doacao = self.__tela_doacao.pega_dados_doacao()
            doacao.data_doacao = novos_dados_doacao["data_doacao"]
            doacao.animal.nome = novos_dados_doacao["nome_animal"]
            doacao.animal.codigo = novos_dados_doacao["codigo_animal"]
            doacao.doador.nome = novos_dados_doacao["nome_doador"]
            doacao.doador.cpf = novos_dados_doacao["cpf_doador"]
            doacao.motivo = novos_dados_doacao["motivo"]
            self.listar_doacoes()

        else:
            self.__tela_doacao.mensagem("Essa doação NÃO EXISTE!")

    def excluir_doacao(self):
        self.listar_doacoes()
        id_doacao = self.__tela_doacao.seleciona_doacao()
        doacao = self.pega_doacao_por_codigo(id_doacao)

        if (doacao is not None):
            self.__doacoes.remove(doacao)
            os.system('cls')
            self.__tela_doacao.mensagem("Doação removida com sucesso!")
        else:
            self.__tela_doacao.mensagem("Esta doação NÃO EXISTE.")

    def listar_doacoes(self):
        if len(self.__doacoes) == 0:
            self.__tela_doacao.mensagem(
                "Ainda não há doações no sistema. Voce deve cadastrar primeiro!")
            self.__controlador_sistema.abre_tela()
        else:
            print("Doações: \n")
            for doador in self.__doacoes:
                self.__tela_doacao.mostra_doacao(
                    {"id": doador.id_doacao,
                        "data_doacao": doador.data_doacao,
                        "nome_doador": doador.doador.nome,
                        "cpf_doador": doador.doador.cpf,
                        "nome_animal": doador.animal.nome,
                        "codigo_animal": doador.animal.codigo,
                        "motivo": doador.motivo})

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_doacao, 2: self.alterar_doacao,
                        3: self.excluir_doacao, 4: self.listar_doacoes,
                        0: "Retornar para menu principal"}
        while True:
            opcao = self.__tela_doacao.tela_opcoes()
            if opcao == 0:
                return
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()
