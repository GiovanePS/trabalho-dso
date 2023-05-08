from telas.tela_adotante import TelaAdotante
from entidades.adotante import Adotante


class ControladorAdotante:
    def __init__(self):
        self.__adotantes = []
        self.__tela_adotante = TelaAdotante()

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
        ...

    def listar_adotantes(self):
        ...

    def abre_tela(self):
        lista_opcoes = {0: "Retornar para menu principal."}

        while True:
            opcao = self.__tela_adotante.abre_tela()
            if opcao == 0:
                return
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()
