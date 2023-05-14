from telas.tela_vacina import TelaVacina
from entidades.vacina import Vacina
import os


class ControladorVacina:
    def __init__(self, controlador_sistema):
        self.__vacinas = []
        self.__tela_vacina = TelaVacina()
        self.__controlador_sistema = controlador_sistema

    @property
    def vacinas(self):
        return self.__vacinas

    def pega_vacina_por_codigo(self, codigo):
        for vacina in self.__vacinas:
            if int(vacina.codigo_vacina) == int(codigo):
                return vacina
        return None

    def incluir_vacina(self):
        self.__tela_vacina.mensagem("Cadastro de Vacina:")
        dados_vacina = self.__tela_vacina.pega_dados_vacina()
        os.system('cls')
        vacina = Vacina( dados_vacina["nome_vacina"],dados_vacina["codigo_vacina"])
        self.__vacinas.append(vacina)
        self.__tela_vacina.mensagem("Vacina cadastrada com sucesso!")

    def alterar_vacina(self):
        self.listar_vacina()
        self.__tela_vacina.mensagem("Alteração cadastral de vacina.")
        codigo = self.__tela_vacina.seleciona_codigo()
        vacina=self.pega_vacina_por_codigo(codigo)
        print()
        if isinstance (vacina, Vacina):
            self.__tela_vacina.mensagem("Novos dados: ")
            novos_dados_vacina = self.__tela_vacina.pega_dados_vacina()
            vacina.nome_vacina= novos_dados_vacina["nome_vacina"]
            vacina.codigo_vacina= novos_dados_vacina["codigo_vacina"]
            os.system('cls')
            self.__tela_vacina.mensagem("Alteração realizada com sucesso!")
        else:
            os.system('cls')
            self.__tela_vacina.mensagem("Vacina inexistente no sistema.")
        print()


    def excluir_vacina(self):
        self.__tela_vacina.mensagem("Exclusão de vacina do sistema.")
        self.listar_vacina()
        codigo = self.__tela_vacina.seleciona_codigo()
        vacina = self.pega_vacina_por_codigo(codigo)
        os.system('cls')
        if isinstance(vacina, Vacina):
            self.__vacinas.remove(vacina)
            self.__tela_vacina.mensagem("Vacina removida com sucesso!")
        else:
            self.__tela_vacina.mensagem("Vacina inexistente no sistema.")
        print()

    def listar_vacina(self):
        if len(self.__vacinas) != 0:
            self.__tela_vacina.mensagem("Lista de vacinas:")
            print()
            for vacina in self.__vacinas:
                self.__tela_vacina.mostra_vacina(vacina)
                print()
        else:
            self.__tela_vacina.mensagem(
                "Ainda não há vacinas no sistema. Você deve cadastrar primeiro!")
            self.__controlador_sistema.abre_tela()
        print()
    def abre_tela(self):
        lista_opcoes = {1: self.incluir_vacina, 2: self.alterar_vacina,
                        3: self.excluir_vacina, 4: self.listar_vacina,
                        0: "Retornar para menu principal."}

        while True:
            opcao = self.__tela_vacina.abre_tela()
            if opcao == 0:
                return
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()
