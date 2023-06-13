from telas.tela_adocao import TelaAdocao
from entidades.adocao import Adocao
import os


class ControladorAdocao:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__adocoes = []
        self.__tela_adocao = TelaAdocao()
        self.__id = 0

    @property
    def adocoes(self):
        return self.__adocoes

    @property
    def tela_adocao(self):
        return self.__tela_adocao

    def pega_adocao_por_id(self, id):
        for adocao in self.__adocoes:
            if int(adocao.id_adocao) == int(id):
                return adocao
        return None

    def incluir_adocao(self):
        self.__controlador_sistema.controlador_adotante.listar_adotantes()
        self.__controlador_sistema.controlador_animal.listar_animais()
        dados_adocao = self.__tela_adocao.pega_dados_adocao()

        adotante = (self.__controlador_sistema.controlador_adotante.pega_adotante_por_cpf(dados_adocao["cpf_adotante"]))  # noqa
        animal = self.__controlador_sistema.controlador_animal.pegar_animal_por_codigo(dados_adocao["codigo_animal_adotado"])# noqa

        if adotante is not None and animal is not None:
            if animal.pode_ser_adotado == True and animal.foi_adotado == False:
                if (animal.tamanho) == ("Grande") and adotante.tipo_habitacao == (
                    "Apartamento pequeno"
                ):
                    self.__tela_adocao.mostra_mensagem(
                        "Pessoas que vivem em apartamentos pequenos não podem adotar cães de porte grande!"
                    )
                    self.__controlador_sistema.abre_tela()
                else:
                    dados_assinatura = self.__tela_adocao.pega_assinatura()
                    self.__id += 1
                    adocao = Adocao(
                        dados_adocao["data_adocao"],
                        animal,
                        adotante,
                        dados_assinatura["assinatura"],
                        self.__id,
                    )
                    self.__adocoes.append(adocao)
                    animal.foi_adotado = True

                    os.system("cls")
                    print("Adoção cadastrada com sucesso!")
            else:
                print(
                    "Este animal não está disponível para adoção"
                )
        else:
            self.__tela_adocao.mostra_mensagem("Dados inválidos!")
        print()

    def alterar_adocao(self):
        self.listar_adocoes()
        id_adocao = self.__tela_adocao.seleciona_adocao()
        adocao = self.pega_adocao_por_id(id_adocao)

        if adocao is not None:
            novos_dados_adocao = self.__tela_adocao.pega_dados_adocao()
            adocao.data_adocao = novos_dados_adocao["data_adocao"]
            adocao.animal_adotado.nome = novos_dados_adocao["nome_animal_adotado"]
            adocao.animal_adotado.codigo = novos_dados_adocao["codigo_animal_adotado"]
            adocao.adotante.nome = novos_dados_adocao["nome_adotante"]
            adocao.adotante.cpf = novos_dados_adocao["cpf_adotante"]
            self.listar_adocoes()

        else:
            self.__tela_adocao.mostra_mensagem("Essa adoção NÃO EXISTE!")

    def excluir_adocao(self):
        self.listar_adocoes()
        id_adocao = self.__tela_adocao.seleciona_adocao()
        adocao = self.pega_adocao_por_id(id_adocao)

        if adocao is not None:
            self.__adocoes.remove(adocao)
            os.system("cls")
            self.__tela_adocao.mostra_mensagem("Adoção removida com sucesso!")
        else:
            self.__tela_adocao.mostra_mensagem("Esta adoção NÃO EXISTE.")

    def listar_adocoes(self):
        if len(self.__adocoes) == 0:
            self.__tela_adocao.mostra_mensagem(
                "Ainda não há adoções no sistema. Voce deve cadastrar primeiro!"
            )
            self.__controlador_sistema.abre_tela()
        else:
            print("Adoções:")
            print()
            for adocao in self.__adocoes:
                self.__tela_adocao.mostra_adocao(adocao)
                print()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_adocao,
            2: self.alterar_adocao,
            3: self.excluir_adocao,
            4: self.listar_adocoes,
            0: "Retornar para menu principal",
        }
        while True:
            opcao = self.__tela_adocao.tela_opcoes()
            if opcao == 0:
                return
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()
