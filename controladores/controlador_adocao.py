from telas.tela_adocao import TelaAdocao
from entidades.adocao import Adocao
from DAOs.adocao_dao import AdocaoDAO


class ControladorAdocao:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__adocao_DAO = AdocaoDAO()
        self.__tela_adocao = TelaAdocao()
        self.__id = 0

    @property
    def adocoes(self):
        return self.__adocao_DAO.get_all()

    @property
    def tela_adocao(self):
        return self.__tela_adocao

    def pega_adocao_por_id(self, id):
        for adocao in self.__adocao_DAO.get_all():
            if int(adocao.id_adocao) == int(id):
                return adocao
        return None

    def incluir_adocao(self):
        if len(self.__controlador_sistema.controlador_adotante.adotantes) == 0:
            self.tela_adocao.mensagem("Ainda não há adotantes no sistema")
            return

        dados_adocao = self.__tela_adocao.pega_dados_adocao()

        if dados_adocao is None:
            self.__tela_adocao.mensagem("Adoção não cadastrada.")
            return

        adotante = (
            self.__controlador_sistema.controlador_adotante.pega_adotante_por_cpf(
                dados_adocao["cpf_adotante"]
            )
        )
        animal = self.__controlador_sistema.controlador_animal.pegar_animal_por_codigo(
            dados_adocao["codigo_animal"]
        )

        if adotante is None:
            self.__tela_adocao.mensagem("Adotante não existente no sistema.")
            return

        if animal is None:
            self.__tela_adocao.mensagem("Animal não existente no sistema.")
            return

        if not animal.pode_ser_adotado and not animal.foi_adotado:
            self.__tela_adocao.mensagem("Este animal não está disponível para adoção pois não tem as vacinas necessárias.")
            return
        elif  animal.pode_ser_adotado and  animal.foi_adotado:
            self.__tela_adocao.mensagem("Este animal já foi adotado, por isso não está mais disponível.")
            return

        if animal.tamanho == "Grande" and adotante.tipo_habitacao == (
            "Apartamento pequeno"
        ):
            self.__tela_adocao.mensagem(
                "Pessoas que vivem em apartamentos pequenos não podem adotar cães de porte grande!"
            )
            return

        dados_assinatura = self.__tela_adocao.pega_assinatura()

        if dados_assinatura is None:
            self.__tela_adocao.mensagem("Adoção não cadastrada.")
            return

        try:
            self.__id = int(list(self.__adocao_DAO.get_all())[-1].id_adocao) + 1
        except IndexError:
            self.__id = 1

        adocao = Adocao(
            dados_adocao["data_adocao"],
            animal,
            adotante,
            dados_assinatura["assinatura"],
            self.__id,
        )
        self.__adocao_DAO.add(adocao)
        animal.foi_adotado = True
        self.__controlador_sistema.controlador_animal.animal_DAO.update(animal)
        self.__tela_adocao.mensagem("Adoção cadastrada com sucesso!")

    def alterar_adocao(self):
        id_adocao = self.__tela_adocao.seleciona_adocao()
        adocao = self.pega_adocao_por_id(id_adocao)

        if adocao is not None:
            novos_dados_adocao = self.__tela_adocao.pega_dados_adocao_alterar()
            adocao.data_adocao = novos_dados_adocao["data_adocao"]
            adocao.animal_adotado.nome = novos_dados_adocao["nome_animal_adotado"]
            adocao.animal_adotado.codigo = novos_dados_adocao["codigo_animal_adotado"]
            adocao.adotante.nome = novos_dados_adocao["nome_adotante"]
            adocao.adotante.cpf = novos_dados_adocao["cpf_adotante"]
            self.__adocao_DAO.update(adocao)
            self.__tela_adocao.mensagem("Adoção alterada com sucesso!")
        else:
            self.__tela_adocao.mensagem("Essa adoção não existe.")

    def excluir_adocao(self):
        id_adocao = self.__tela_adocao.seleciona_adocao()
        adocao = self.pega_adocao_por_id(id_adocao)

        if adocao is not None:
            self.__adocao_DAO.remove(adocao.id_adocao)
            self.__tela_adocao.mensagem("Adoção removida com sucesso!")
        else:
            self.__tela_adocao.mensagem("Esta adoção não existe.")

    def listar_adocoes(self):
        if len(self.__adocao_DAO.get_all()) == 0:
            self.__tela_adocao.mensagem("Ainda não há adoções no sistema.")
        else:
            dados_adocoes = []
            for adocao in self.__adocao_DAO.get_all():
                dados_adocoes.append(
                    {
                        "id_adocao": adocao.id_adocao,
                        "data_adocao": adocao.data_adocao,
                        "animal_adotado_nome": adocao.animal_adotado.nome,
                        "animal_adotado_codigo": adocao.animal_adotado.codigo,
                        "adotante_nome": adocao.adotante.nome,
                        "adotante_cpf": adocao.adotante.cpf,
                        "assinatura": adocao.assinatura,
                    }
                )

            self.__tela_adocao.mostra_adocao(dados_adocoes)

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_adocao,
            2: self.alterar_adocao,
            3: self.excluir_adocao,
            4: self.listar_adocoes,
            0: "Retornar para menu principal",
        }
        while True:
            opcao = self.__tela_adocao.abre_tela()
            if opcao == 0:
                return
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()
