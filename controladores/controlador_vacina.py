from telas.tela_vacina import TelaVacina
from entidades.vacina import Vacina
from DAOs.vacina_dao import VacinaDAO


class ControladorVacina:
    def __init__(self, controlador_vacinacao):
        self.__vacina_DAO = VacinaDAO()
        self.__codigo = 0
        self.__tela_vacina = TelaVacina()
        self.__controlador_vacinacao = controlador_vacinacao

    @property
    def vacinas(self):
        return self.__vacina_DAO.get_all()

    @property
    def controlador_vacinacao(self):
        return self.__controlador_vacinacao

    def pega_vacina_por_codigo(self, codigo):
        for vacina in self.__vacina_DAO.get_all():
            if int(vacina.codigo_vacina) == int(codigo):
                return vacina
        return None

    def incluir_vacina(self):
        dados_vacina = self.__tela_vacina.pega_dados_vacina()
        if dados_vacina is None:
            self.__tela_vacina.mensagem("Vacina não cadastrada.")
            return

        for vacina in self.vacinas:
            if (vacina.nome_vacina).upper() == dados_vacina['nome_vacina'].upper():
                self.__tela_vacina.mensagem("Esta vacina já está cadastrada.")
                return

        try:
            self.__codigo = int(list(self.__vacina_DAO.get_all())[-1].codigo_vacina) + 1
        except IndexError:
            self.__codigo = 1
        vacina = Vacina(dados_vacina["nome_vacina"], self.__codigo)
        self.__vacina_DAO.add(vacina)
        self.__tela_vacina.mensagem("Vacina cadastrada com sucesso!")

    def alterar_vacina(self):
        codigo = self.__tela_vacina.seleciona_codigo()
        vacina = self.pega_vacina_por_codigo(codigo)
        if isinstance(vacina, Vacina):
            novos_dados_vacina = self.__tela_vacina.pega_dados_vacina()
            if novos_dados_vacina is None:
                self.__tela_vacina.mensagem("Vacina não alterada.")
                return

            vacina.nome_vacina = novos_dados_vacina["nome_vacina"]
            self.__vacina_DAO.update(vacina)
            self.__tela_vacina.mensagem("Alteração realizada com sucesso!")
        else:
            self.__tela_vacina.mensagem("Vacina inexistente no sistema.")

    def excluir_vacina(self):
        codigo = self.__tela_vacina.seleciona_codigo()
        vacina = self.pega_vacina_por_codigo(codigo)
        if isinstance(vacina, Vacina):
            self.__vacina_DAO.remove(vacina.codigo_vacina)
            self.__tela_vacina.mensagem("Vacina removida com sucesso!")
        else:
            self.__tela_vacina.mensagem("Vacina inexistente no sistema.")

    def listar_vacina(self):
        if len(self.__vacina_DAO.get_all()) != 0:
            dados_vacinas = []
            for vacina in self.__vacina_DAO.get_all():
                dados_vacinas.append({
                    "nome": vacina.nome_vacina,
                    "codigo": vacina.codigo_vacina
                })

            self.__tela_vacina.mostra_vacina(dados_vacinas)
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
