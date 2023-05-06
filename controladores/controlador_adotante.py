from telas.tela_adotante import TelaAdotante


class ControladorAdotante:
    def __init__(self):
        self.__adotantes = []
        self.__tela_adotante = TelaAdotante()

    def incluir_adotante(self):
        ...

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
