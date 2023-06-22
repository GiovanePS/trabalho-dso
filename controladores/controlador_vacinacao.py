from telas.tela_vacinacao import TelaVacinacao
from entidades.vacinacao import Vacinacao
from DAOs.vacinacao_dao import VacinacaoDAO
from controladores.controlador_vacina import ControladorVacina
import os


class ControladorVacinacao:
    def __init__(self, controlador_sistema):
        self.__vacinacao_DAO= VacinacaoDAO()
        self.__controlador_sistema = controlador_sistema
        self.__controlador_vacina = ControladorVacina(self)
        self.__tela_vacinacao = TelaVacinacao()
        if len(self.__vacinacao_DAO.get_all()) == 0:
            self.__id = 0
        else:
            self.__id = int(list(self.__vacinacao_DAO.get_all())[-1].id_vacinacao)

    
    @property
    def vacinacoes(self):
        return self.__vacinacao_DAO.get_all()

    def pega_vacinacao_por_id(self, id):
        for vacinacao in self.__vacinacao_DAO.get_all():
            if int(vacinacao.id_vacinacao) == int(id):
                return vacinacao
        return None

    def incluir_vacinacao(self):
        self.__controlador_vacina.listar_vacina()
        self.__controlador_sistema.controlador_animal.listar_animais()
        dados_vacinacao = self.__tela_vacinacao.pega_dados_vacinacao()

        vacina = self.__controlador_vacina.pega_vacina_por_codigo(
            dados_vacinacao["codigo_vacina"]
        )  # noqa
        animal = self.__controlador_sistema.controlador_animal.pegar_animal_por_codigo(
            dados_vacinacao["codigo_animal_vacinado"]
        )  # noqa

        if vacina is not None and animal is not None:
            self.__id += 1
            vacinacao = Vacinacao(
                dados_vacinacao["data_vacinacao"], vacina, animal, self.__id
            )

            self.__vacinacao_DAO.add(vacinacao)
            
            os.system("cls")
            animal.vacinas.append(vacina.nome_vacina)
            print("Vacinação registrada com sucesso!")
            if (
                "Raiva" in animal.vacinas
                and "Leptospirose" in animal.vacinas
                and "Hepatite Infecciosa" in animal.vacinas
            ):
                animal.pode_ser_adotado = True
        else:
            self.__tela_vacinacao.mensagem("Dados inválidos!")


    def alterar_vacinacao(self):
        self.listar_vacinacoes()
        id_vacinacao = self.__tela_vacinacao.seleciona_vacinacao()
        vacinacao = self.pega_vacinacao_por_id(id_vacinacao)

        if vacinacao is not None:
            novos_dados_vacinacao = self.__tela_vacinacao.pega_dados_vacinacao()
            vacinacao.data_vacinacao = novos_dados_vacinacao["data_vacinacao"]
            vacinacao.animal.codigo = novos_dados_vacinacao["codigo_animal_vacinado"]
            vacinacao.vacina.codigo_vacina = novos_dados_vacinacao["codigo_vacina"]
            self.listar_vacinacoes()

        else:
            self.__tela_vacinacao.mensagem(
                "Essa vacinação NÃO está registrada neste sistema!"
            )

    def excluir_vacinacao(self):
        id_vacinacao = self.__tela_vacinacao.seleciona_vacinacao()
        vacinacao = self.pega_vacinacao_por_id(id_vacinacao)

        if vacinacao is not None:
            self.__vacinacao_DAO.remove(vacinacao.id_vacinacao)
            self.__tela_vacinacao.mensagem("Vacinação removida com sucesso!")
        else:
            self.__tela_vacinacao.mensagem(
                "Esta vacinação NÃO está registrada neste sistema."
            )

    def listar_vacinacoes(self):
        if len(self.__vacinacao_DAO.get_all()) == 0:
            self.__tela_vacinacao.mensagem(
                "Ainda não há vacinações no sistema. Voce deve cadastrar primeiro!"
            )
            self.__controlador_sistema.abre_tela()
        else:
            dados_vacinacoes = []
            for vacinacao in self.__vacinacao_DAO.get_all():
                dados_vacinacoes.append({
                        "codigo_vacinacao": vacinacao.id_vacinacao,
                        "data_vacinacao": vacinacao.data_vacina,
                        "nome_animal": vacinacao.animal.nome,
                        "codigo_animal": vacinacao.animal.codigo,
                        "nome_vacina": vacinacao.vacina.nome_vacina,
                        "codigo_vacina": vacinacao.vacina.codigo_vacina,
                })

            self.__tela_vacinacao.mostra_vacinacao(dados_vacinacoes)

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_vacinacao,
            2: self.alterar_vacinacao,
            3: self.excluir_vacinacao,
            4: self.listar_vacinacoes,
            5: self.__controlador_vacina.abre_tela,
            0: "Retornar para menu principal",
        }
        while True:
            opcao = self.__tela_vacinacao.abre_tela()
            if opcao == 0:
                return
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()
