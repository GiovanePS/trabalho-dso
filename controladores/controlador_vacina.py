from telas.tela_vacina import TelaVacina
from entidades.vacina import Vacina
from DAOs.vacina_dao import VacinaDAO
import os


class ControladorVacina:
    def __init__(self, controlador_vacinacao):
        self.__vacina_DAO = VacinaDAO()
        self.__tela_vacina = TelaVacina()
        self.__controlador_vacinacao = controlador_vacinacao
        self.__codigos = []

    @property
    def vacinas(self):
        return self.__vacina_DAO.get_all()

    def pega_vacina_por_codigo(self, codigo):
        for vacina in self.__vacina_DAO.get_all():
            if int(vacina.codigo_vacina) == int(codigo):
                return vacina
        return None

    def incluir_vacina(self):
        self.__tela_vacina.mensagem("Cadastro de Vacina:")
        while True:
            dados_vacina = self.__tela_vacina.pega_dados_vacina()
            if dados_vacina["codigo_vacina"] in self.__codigos:
                self.__tela_vacina.mensagem(
                    "Este código já está cadastrado como o de outra"
                    " vacina, por favor insira outro valor."
                )
            else:
                break
        os.system("cls")
        vacina = Vacina(dados_vacina["nome_vacina"], dados_vacina["codigo_vacina"])
        self.__codigos.append(dados_vacina["codigo_vacina"])
        self.__vacina_DAO.add(vacina)
        self.__tela_vacina.mensagem("Vacina cadastrada com sucesso!")
        print()

    def alterar_vacina(self):
        self.listar_vacina()
        self.__tela_vacina.mensagem("Alteração cadastral de vacina.")
        codigo = self.__tela_vacina.seleciona_codigo()
        vacina = self.pega_vacina_por_codigo(codigo)
        print()
        if isinstance(vacina, Vacina):
            self.__tela_vacina.mensagem("Novos dados: ")
            novos_dados_vacina = self.__tela_vacina.pega_dados_vacina()
            vacina.nome_vacina = novos_dados_vacina["nome_vacina"]
            vacina.codigo_vacina = novos_dados_vacina["codigo_vacina"]
            os.system("cls")
            self.__tela_vacina.mensagem("Alteração realizada com sucesso!")
        else:
            os.system("cls")
            self.__tela_vacina.mensagem("Vacina inexistente no sistema.")
        print()

    def excluir_vacina(self):
        self.__tela_vacina.mensagem("Exclusão de vacina do sistema.")
        self.listar_vacina()
        codigo = self.__tela_vacina.seleciona_codigo()
        vacina = self.pega_vacina_por_codigo(codigo)
        os.system("cls")
        if isinstance(vacina, Vacina):
            self.__vacina_DAO.remove(vacina)
            self.__tela_vacina.mensagem("Vacina removida com sucesso!")
            self.__codigos.remove(codigo)
        else:
            self.__tela_vacina.mensagem("Vacina inexistente no sistema.")
        print()

    def listar_vacina(self):
        if len(self.__vacina_DAO.get_all()) != 0:
            self.__tela_vacina.mensagem("Lista de vacinas (código - vacina):")
            print()
            for vacina in self.__vacina_DAO.get_all():
                self.__tela_vacina.mostra_vacina(vacina)
                print()
        else:
            self.__tela_vacina.mensagem("Ainda não há vacinas no sistema. ")

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_vacina,
            2: self.alterar_vacina,
            3: self.excluir_vacina,
            4: self.listar_vacina,
            0: "Retornar para menu principal.",
        }

        while True:
            opcao = self.__tela_vacina.abre_tela()
            if opcao == 0:
                return
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()
