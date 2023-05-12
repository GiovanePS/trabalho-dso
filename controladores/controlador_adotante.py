from telas.tela_adotante import TelaAdotante
from entidades.adotante import Adotante
import os


class ControladorAdotante:
    def __init__(self):
        self.__adotantes = []
        self.__tela_adotante = TelaAdotante()

    def pega_adotante_por_cpf(self):
        ...

    def incluir_adotante(self):
        dados_adotante = self.__tela_adotante.pega_dados()
        adotante = Adotante(dados_adotante["cpf"],
                            dados_adotante["nome"],
                            dados_adotante["data_nascimento"],
                            dados_adotante["endereco"],
                            dados_adotante["tipo_habitacao"],
                            dados_adotante["tem_animais"])
        self.__adotantes.append(adotante)

    def alterar_adotante(self):
        ...

    def excluir_adotante(self):
        self.__tela_adotante.mensagem("Exclusão de adotante do sistema.")
        cpf = self.__tela_adotante.seleciona_cpf()
        adotante = self.pega_adotante_por_cpf(cpf)
        if isinstance(adotante, Adotante):
            self.__adotantes.remove(adotante)
            self.__tela_adotante.mensagem("Adotante removido com sucesso!")
        else:
            self.__tela_adotante.mensagem("Adotante inexistente no sistema.")
        os.system('cls')

    def listar_adotantes(self):
        self.__tela_adotante.mensagem("Lista de adotantes:")

    def abre_tela(self):
        lista_opcoes = {0: "Retornar para menu principal."}

        while True:
            opcao = self.__tela_adotante.abre_tela()
            if opcao == 0:
                return
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()
